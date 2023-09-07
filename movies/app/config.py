import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path=dotenv_path)



class Config:
    TMDB_API_KEY = os.environ.get("TMDB_API_KEY")
    SQLALCHEMY_URI = os.environ.get("SQLALCHEMY_URI")
