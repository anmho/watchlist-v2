from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, Depends
from .services.users import UserService
from typing import Annotated, Any, Dict, Union
import logging


app = FastAPI()


class UserCreate(BaseModel):
    email: EmailStr

@app.get("/users")
def get_users(
    userService: Annotated[UserService, Depends()],
    ):

    # userCreate.model_
    # userService.create_user()
    # return userCreate
    return {}


@app.post("/users")
def create_user(
        userService: Annotated[UserService, Depends()], 
        userCreate: UserCreate
    ):
    print(userCreate)
    print(userCreate.model_dump())

    user = userService.create_user(**userCreate.model_dump(include=['email']))

    return user

@app.get("/users/{user_id}")
def get_user(
        user_id: str,
        userService: Annotated[UserService, Depends()]
    ):

    user = userService.get_user(user_id)
    return user




