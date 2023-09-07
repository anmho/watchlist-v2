from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, Depends
from .services.users import UserService
from typing import Annotated, Any, Dict, Union
import logging

from .proto.user_pb2_grpc import UsersStub
from .proto.user_pb2 import CreateUserRequest
import grpc 


app = FastAPI()

channel = grpc.insecure_channel("127.0.0.1:50051")
client = UsersStub(channel)


class UserCreate(BaseModel):
    email: EmailStr

@app.get("/users")
def get_users(
    userService: Annotated[UserService, Depends()],
    ):

    # userCreate.model_
    # userService.create_user()
    # return userCreate

    request = CreateUserRequest(email="hello@a.com")

    response = client.CreateUser(request)
    print(response)
    return {"email": response.user.email}


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




