import sqlalchemy
from sqlalchemy.orm import Session, Query



import logging
import psycopg2
from app.models.ratings.tables import Rating


class RatingService:
    logger = logging.getLogger("RatingService")

    @classmethod
    def get_ratings(cls, user_id: str, movie_id: str, db: Session) -> Query[Rating]:
        query = db.query(Rating)

        if user_id:
            query = query.filter_by(user_id=user_id)

        if movie_id:
            query = query.filter_by(movie_id=movie_id)

        return query.all()



    @classmethod
    def create_rating(cls, user_id: str, rating: float, movie_id: str, db: Session):
        try:
            rating = Rating(user_id=user_id, rating=rating, movie_id=movie_id)

            db.add(rating)
            db.commit()

        except sqlalchemy.exc.IntegrityError as e:
            cls.logger.error(e)
            db.rollback()
            raise   
        except psycopg2.errors.UniqueViolation as e:
            cls.logger.error(e)
            db.rollback()
            raise
        except Exception as e:
            cls.logger.error(e)
            db.rollback()
            raise

        return rating

    @classmethod
    def update_rating(cls, user_id: str, rating: float, movie_id: str, db: Session) -> Rating:

        rating_obj = db.query(Rating).filter_by(user_id=user_id, movie_id=movie_id).first()

        rating_obj.rating = rating
        db.commit()

        db.refresh(rating_obj)

        return rating_obj