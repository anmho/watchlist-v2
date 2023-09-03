from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import sqlalchemy
from app.models.tokens.dto import RefreshTokenResponse
from app.services.blacklist import BlacklistService
from app.models.users.dto import CreateUserRequest, CreateUserResponse
from app.models.database import Session
from app.models.users.tables import User
from logging import Logger
from app.services.tokens import TokenService
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


def basic_auth_required(credentials: HTTPBasicCredentials = Depends(basic_auth)) -> User:
    # Check if user with email exists
    email = credentials.username
    password = credentials.password

    with Session() as session:
        user: User = session.query(User).filter_by(email=email).first()
        if not user or not user.verify_password(password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        return user


@auth.post("/register")
async def register_email_pw(createUserDto: CreateUserRequest) -> CreateUserResponse:
    email, password = createUserDto.email, createUserDto.password

    user = None

    with Session() as session:
        try:
            # Create the user
            user = User(email=email, registration_type="standard")
            user.set_password(password)
            session.add(user)
            session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            # Rollback if error occurred
            logger.error(e)
            session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"user with {email=} already exists")
        except Exception as e:
            # Rollback if error occured
            logger.error(e)
            session.rollback()

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        logger.debug(user)
        access_token = TokenService.create_access(sub=str(user.id))
        refresh_token = TokenService.create_refresh(sub=str(user.id))

        data = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

        response = JSONResponse(
            content=data, status_code=status.HTTP_201_CREATED)

        return response


@auth.post("/tokens")
def login_email_pw(user: User = Depends(basic_auth_required)):
    """ gets access and refresh with email and password """

    data = {
        "access_token": TokenService.create_access(str(user.id)),
        "refresh_token": TokenService.create_refresh(str(user.id))
    }

    response = JSONResponse(content=data, status_code=status.HTTP_201_CREATED)

    return response


@auth.post("/refresh")
def refresh(refresh_token: str = Depends(oauth2_scheme)) -> RefreshTokenResponse:
    """ Verifies refresh_token and returns access token"""
    if not TokenService.check_token(refresh_token):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    claims = TokenService.decode(refresh_token)

    if claims['token_type'] != 'refresh':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    access_token = TokenService.create_access(claims['sub'])

    data = {
        "access_token": access_token
    }

    response = JSONResponse(content=data, status_code=201)

    return response


@auth.post("/revoke")
def revoke(token: str = Depends(oauth2_scheme)):
    """ adds the token to a blacklist """
    BlacklistService.add(token)
    return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)
