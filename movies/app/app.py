from fastapi import FastAPI
from app.routes.movies import movies
from app.routes.ratings import ratings
from app.utils.logger import LoggerFactory
import logging


logging.basicConfig(level=logging.DEBUG)
LoggerFactory.set_level(logging.DEBUG)


def create_app():
    app = FastAPI()

    # Register routers
    app.include_router(movies)
    app.include_router(ratings)




    return app
