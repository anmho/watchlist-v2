from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

engine = create_engine('postgresql://admin:admin@localhost:5433/dev')

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


async def use_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Engine
# Base
# Sessionmaker
# db hook