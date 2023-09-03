from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: Optional[str]


class CreateUserResponse(BaseModel):
    access_token: str
    refresh_token: str


class UpdateUserDto(BaseModel):
    pass

