from enum import Enum
from dotenv import load_dotenv
from os.path import join, dirname
import os


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

# Prod Config
# Dev Config


class Environment(Enum):
    PRODUCTION = 1
    DEVELOPMENT = 2


ENVIRONMENT = Environment.DEVELOPMENT


class Config:
    DEBUG = ENVIRONMENT == Environment.DEVELOPMENT
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
    GOOGLE_AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
    REDIS_HOST = os.environ.get("REDIS_HOST")
    REDIS_PORT = os.environ.get("REDIS_PORT")
