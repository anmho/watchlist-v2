from app.models.database import Base, engine
import logging


def main():
    logging.info("Deleting tables...")
    Base.metadata.drop_all(bind=engine)
    logging.info("...Deleted tables")


if __name__ == "__main__":
    main()
