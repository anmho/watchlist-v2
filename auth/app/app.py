from fastapi import FastAPI
from starlette.config import Config as starlette_config

from app.decorators.auth import protected
from authlib.integrations.starlette_client import OAuth
from redis import Redis
import logging

from app.utils.logger import LoggerFactory
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from starlette.middleware.sessions import SessionMiddleware
from app.config import Config


logging.basicConfig(level=logging.DEBUG)
LoggerFactory.configure(level=logging.DEBUG)
limiter = Limiter(key_func=get_remote_address, enabled=False)

oauth = OAuth(starlette_config(".env"))
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)


def create_app():
    app = FastAPI()
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    # Add Middlewares
    app.add_middleware(SessionMiddleware, secret_key=Config.SECRET_KEY)

    from app.routers.auth import auth
    # Register routers
    app.include_router(auth)
    app.include_router(protected)

    return app
