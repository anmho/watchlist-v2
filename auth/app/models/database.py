from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import Config
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass


print(Config.SQLALCHEMY_DATABASE_URI)

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
