from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
import psycopg2
import sqlalchemy
import logging
from sqlalchemy.orm import Session
from app.models.database import Session, get_db
from app.models.ratings.dto import CreateRatingRequest, UpdateRatingRequest
from app.models.ratings.tables import Rating

from app.services.ratings import RatingService



ratings = APIRouter(
    prefix="/ratings",
    tags=["ratings"],
    dependencies=[]
)
logger = logging.getLogger(__name__)

@ratings.get("")
def get_ratings(user_id: str = None, movie_id: str = None, db: Session = Depends(get_db)):
    return RatingService.get_ratings(user_id, movie_id, db)

@ratings.post("")
def submit_rating(createRatingRequest: CreateRatingRequest, db: Session = Depends(get_db)):
    user_id = createRatingRequest.user_id
    rating_score = createRatingRequest.rating
    movie_id = createRatingRequest.movie_id
    # Does the rating exist
    ratings = RatingService.get_ratings(user_id, movie_id, db)
    if ratings:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="rating already exists")
    

    try:
        rating = RatingService.create_rating(
            user_id=user_id, 
            rating=rating_score, 
            movie_id=movie_id, 
            db=db)
        logger.debug(rating)
        return rating
    except sqlalchemy.exc.IntegrityError as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    


@ratings.put("")
def edit_rating(updateRatingRequest: UpdateRatingRequest, db: Session = Depends(get_db)) :
    user_id = updateRatingRequest.user_id
    rating_score = updateRatingRequest.rating
    movie_id = updateRatingRequest.movie_id

    rating = RatingService.get_ratings(user_id=user_id, movie_id=movie_id, db=db)

    if not rating:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="rating not found")
    

    try:
        rating = RatingService.update_rating(user_id=user_id, rating=rating_score, movie_id=movie_id, db=db)
    except sqlalchemy.exc.IntegrityError as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return rating
    