from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from pytest import Session

from app.models.users.tables import User
from app.services.tokens import TokenService


basic_auth = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="tokens")


def basic_auth_required(credentials: HTTPBasicCredentials = Depends(basic_auth)) -> User:
    # Check if user with email exists
    email = credentials.username
    password = credentials.password

    with Session() as session:


        
        if not user or not user.verify_password(password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        return user


def token_auth_required(token: str = Depends(oauth2_scheme)) -> User:
    if not TokenService.check_token(token):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    
