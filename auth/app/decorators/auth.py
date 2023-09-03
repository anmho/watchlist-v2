from fastapi import Request, HTTPException, status, Depends
from functools import wraps
import hashlib
import base64
from fastapi.routing import APIRouter
import logging
import string
from app.models.database import Session
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials


protected = APIRouter()


# def basic_auth_required(func):

#     @wraps(func)
#     def wrapper(request, *args, **kwargs):

#         try:
#             auth: str = request.headers.get("Authorization")
#             auth = auth.removeprefix("Basic ")
#             auth = base64.b64decode(auth).decode("utf-8")

#             email, password = auth.split(":")

#             result = func(request, email, *args, **kwargs)

#             return result

#         except Exception as e:
#             logging.error(e)

#             raise HTTPException(staatus_code=status.HTTP_401_UNAUTHORIZED)

#     return wrapper


# @protected.get("/protected")
# # @basic_auth_required
# def protected_route(request: Request, email: str):
#     print(email)

#     return {"Hello": "Hello"}

# def token_auth_required(func)
