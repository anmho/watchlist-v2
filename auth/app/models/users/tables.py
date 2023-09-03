from uuid import uuid4
from pydantic import BaseModel, EmailStr
from sqlalchemy import Uuid, String
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer
from app.models.database import Base
import bcrypt


class User(Base):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(Uuid, primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[Optional[str]] = mapped_column(String(128))
    registration_type: Mapped[str]

    def set_password(self, password: str):
        pw_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode('utf-8')
        self.password = pw_hash

    def verify_password(self, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def __repr__(self):
        return f"User(id={self.id=} email={self.email})"
