from flask import Flask
from .config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
import logging

cors = CORS()
db = SQLAlchemy()
oauth = OAuth()

def create_app():
    app = Flask(__name__)
    # Configurations
    app.config.from_object(Config)
    # Extensions
    cors.init_app(app)
    db.init_app(app)
    oauth.init_app(app)

    # CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=Config.GOOGLE_CLIENT_ID,
        client_secret=Config.GOOGLE_CLIENT_SECRET,
        server_metadata_url= 'https://accounts.google.com/.well-known/openid-configuration',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        client_kwargs={'scope': 'email profile'},
        authorize_params={'access_type': 'offline'},

    )

    if app.config["DEBUG"]:
        logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s - %(name)s - %(levelname)s] %(message)s]"
        )
    else:
        logging.basicConfig(
            level=logging.WARNING,
            format="[%(asctime)s - %(name)s - %(levelname)s- %(message)s]"
        )


    # Blueprints
    from .views import auth
    app.register_blueprint(auth, url_prefix="/auth")

    return app