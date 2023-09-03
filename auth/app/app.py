from fastapi import FastAPI
from http.client import HTTPException
import json
from flask import Flask

from app.decorators.auth import protected
from .config import Config
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
from redis import Redis
import logging
from app.routers.auth import auth
from app.utils.logger import LoggerFactory


# cors = CORS()
# oauth = OAuth()
# redis = Redis(
#     host=Config.REDIS_HOST,
#     port=Config.REDIS_PORT,
#     decode_responses=True
# )

logging.basicConfig(level=logging.DEBUG)
LoggerFactory.configure(level=logging.DEBUG)


def create_app():
    # app = Flask(__name__)
    app = FastAPI()

    # Register routers
    app.include_router(auth)
    app.include_router(protected)

    return app
