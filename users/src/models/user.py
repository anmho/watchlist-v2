from typing import List
from .database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Uuid, ForeignKey, CheckConstraint, PrimaryKeyConstraint
from uuid import uuid4

class User(Base):
    __tablename__ = 'users'

    id: Mapped[str] = mapped_column(Uuid, primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(unique=True)
    ratings: Mapped[List["Rating"]] = relationship(back_populates='user', cascade="all, delete-orphan")

class Rating(Base):
    __tablename__ = 'ratings'

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="ratings")
    rating: Mapped[float]
    movie_id: Mapped[str]

    __table_args__ = (
        CheckConstraint('rating >= 0 AND rating <= 5', 'rating_constraint'),
        PrimaryKeyConstraint('user_id', 'movie_id')
    )
