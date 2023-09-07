from pydantic import BaseModel





class CreateRatingRequest(BaseModel):
    user_id: str
    rating: float
    movie_id: str
    


class UpdateRatingRequest(BaseModel):
    user_id: str
    rating: float
    movie_id: str