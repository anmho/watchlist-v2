from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import sqlalchemy
from app.models.tokens.dto import RefreshTokenResponse
from app.routers.utils import basic_auth_required
from app.services.blacklist import BlacklistService
from app.models.users.dto import CreateUserRequest, CreateUserResponse
from app.models.database import Session, get_db
from app.models.users.tables import User
from logging import Logger
from app.services.tokens import TokenService
from app.services.users import UserService
from app.utils.logger import LoggerFactory
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer


auth = APIRouter()
logger = LoggerFactory.create(__name__)


""" 
Registers user with email and password. 
Returns JWT on success

200: Success
401: Account with email already exists
"""

basic_auth = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="tokens")


@auth.post("/register")
async def register_email_pw(
    createUserDto: CreateUserRequest,
    db: Session = Depends(get_db)
) -> CreateUserResponse:
    email, password = createUserDto.email, createUserDto.password

    # Does the user exist
    user = UserService.get_user_by_email(email=email, session=db)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"user with {email=} already exists")

    try:
        user = UserService.create_user(
            email=email, password=password, session=db)
    except sqlalchemy.exc.IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR) from e

    user_id = str(user.id)
    access_token = TokenService.create_access(user_id)
    refresh_token = TokenService.create_refresh(user_id)

    data = CreateUserResponse(
        access_token=access_token, refresh_token=refresh_token)

    response = JSONResponse(
        content=data.model_dump(), status_code=status.HTTP_201_CREATED)
    return response


@auth.post("/tokens")
def login_email_pw(user: User = Depends(basic_auth_required)):
    """ gets access and refresh with email and password. used for signing in on a client """

    data = {
        "access_token": TokenService.create_access(str(user.id)),
        "refresh_token": TokenService.create_refresh(str(user.id))
    }

    response = JSONResponse(content=data, status_code=status.HTTP_201_CREATED)

    return response


@auth.post("/refresh")
def refresh(refresh_token: str = Depends(oauth2_scheme)) -> RefreshTokenResponse:
    """ Verifies refresh_token and returns access token. used for refreshing the login of a user """

    # abstract this to a function
    if not TokenService.check_token(refresh_token):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if BlacklistService.contains(refresh_token):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    claims = TokenService.decode(refresh_token)

    if claims['token_type'] != 'refresh':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    access_token = TokenService.create_access(claims['sub'])
    data = {"access_token": access_token}

    return JSONResponse(content=data, status_code=201)


@auth.post("/revoke")
def revoke(token: str = Depends(oauth2_scheme)):
    """ adds the token to a blacklist """
    BlacklistService.add(token)
    return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)
