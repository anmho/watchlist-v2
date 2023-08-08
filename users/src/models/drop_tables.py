from .database import Base, engine
from .user import User, Rating

if __name__ == "__main__":
    Base.metadata.drop_all(bind=engine)