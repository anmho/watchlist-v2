from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.config import Config


class Base(DeclarativeBase):
    pass


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)


# Must be at bottom to prevent circular import
from .user_credentials import CreateUserCredentials, UserCredential
