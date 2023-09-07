from app.config import Config
from app.models.database import Base, engine

def main():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()