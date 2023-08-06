from src.config import Config
from . import Base, engine


def main():
    print(Config.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
