from pydantic import BaseModel, EmailStr
from sqlalchemy import Uuid, String
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer
from . import Base


class CreateUserCredentials(BaseModel):
    email: EmailStr
    password: Optional[str]


class UserCredential(Base):
    __tablename__ = 'user_credentials'

    id: Mapped[str] = mapped_column(Uuid, primary_key=True)
    email: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[Optional[str]] = mapped_column(String(128))
