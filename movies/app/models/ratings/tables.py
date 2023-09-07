from app.models.database import Base
from sqlalchemy import CheckConstraint, PrimaryKeyConstraint, Uuid
from sqlalchemy.orm import Mapped, mapped_column



class Rating(Base):
    __tablename__ = "ratings"

    user_id: Mapped[str] = mapped_column(Uuid, nullable=False)
    rating: Mapped[float] =  mapped_column(nullable=False)
    movie_id: Mapped[str] = mapped_column(nullable=False)

    __table_args__ = (
        CheckConstraint('rating >= 0 AND rating <= 5', 'rating_constraint'),
        PrimaryKeyConstraint("user_id", "movie_id")
    )


    def __repr__(self):
        return f"<Rating(user_id={self.user_id}, rating={self.rating}, movie_id={self.movie_id})>"
        











