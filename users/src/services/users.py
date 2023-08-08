from typing import Union
from fastapi import Depends
from sqlalchemy.orm import Session
from ..models.database import use_db
from ..models import User, Rating
import logging
from psycopg2.errors import IntegrityError


class RatingService:
    def __init__(self, db: Session = Depends(use_db)):
        self.db = db

    def create_rating(self):
        pass

    def update_rating(self):
        pass


class UserService:
    def __init__(self, db: Session = Depends(use_db)):
        self.db = db

    def create_user(self, email: str):
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
        # return self.db.get(User, ident=id)
        

    def get_users(self):
        pass

    def add_rating(self):
        pass

    



