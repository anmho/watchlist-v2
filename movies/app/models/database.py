from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from sqlalchemy import create_engine
from app.config import Config

class Base(DeclarativeBase):
    pass

engine = create_engine(Config.SQLALCHEMY_URI, echo=True)
DBSession: Session  = sessionmaker(bind=engine)

async def get_db():
    db: Session = DBSession()

    try:
        yield db

    finally: 
        db.close()