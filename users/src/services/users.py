from typing import Union
from fastapi import Depends
from sqlalchemy.orm import Session
from ..models.database import SessionLocal, use_db
from ..models import User, Rating
import logging
from psycopg2.errors import IntegrityError

from ..models import 


class RatingService:
    def __init__(self, db: Session):
        self.db = db

    def create_rating(self, user_id: str, rating: float, movie_id: str):

        # Check the user exists

        # Check the rating exists

        # Check the movie exists



        try:
            rating = Rating(user_id=user_id, rating=rating, movie_id=movie_id)


        except Exception as e:
            self.db.rollback()

    def update_rating(self):
        pass


class UserService:
    def create_user(self, email: str, db: Session):
        self.db = db
        user = User(
            email=email
        )
        # should be here since its the business logic

        try:
            self.db.add(user)
            self.db.commit()
        except Exception as e:
            logging.error(e)
            self.db.rollback()
            raise
        return user

    def get_user(self, id: str) -> Union[User, None]:
        return self.db.query(User).get(ident=id)
        

    def get_users(self, **filters):
        return self.db.query(User).all(**filters)

    def add_rating(self, user_id: str, rating: float, movie_id: int):
        rating = Rating(user_id=user_id, rating=rating, movie_id=movie_id)
        

    



