from pydantic import ValidationError
from werkzeug.exceptions import NotFound, BadRequest, Forbidden, InternalServerError, UnsupportedMediaType
import binascii
from flask import Blueprint, session, redirect, request, url_for, abort, jsonify
from requests import codes
import logging
from src.services.auth_service import parse_basic_auth
from src.app import oauth
from src.config import Config
import logging
import requests
from pprint import pprint
from ..config import Config
from requests import PreparedRequest, Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from src.services.oauth_service import GoogleOAuthService
from authlib.integrations.requests_client import OAuth2Session
import base64
import traceback
from ..models import CreateUserCredentials, UserCredential, Session

auth = Blueprint('auth', __name__)

# @basic_auth_required


@auth.route('/login', methods=['POST'])
def login():
    """
    Validates user credentials (username + password) and returns a JWT access_token and refresh_token
    """

    return {"Hello": "World"}, 200


@auth.route('/signup', methods=['POST'])
def sign_up():
    """
    1) Check that for valid username and password (alongside client checking)
    1) Create a new user
    3) Generate an access token and refresh token for the user
    4) Handle login redirection on client side
    """

    # Try to parse the body
    parsed_user_creds = None
    try:
        body = request.get_json()
        create_user_dto = CreateUserCredentials(**body)
        parsed_user_creds = create_user_dto.model_dump_json()

    except ValidationError as e:
        print(e.json())
        raise BadRequest("bad request", response={"errors": e.errors()})
    except UnsupportedMediaType as e:
        logging.error(e)
        raise UnsupportedMediaType("body must be application/json") from e

    # Create the user credentials in the database

    with Session() as session:
        try:
            user_credentials = UserCredential(**parsed_user_creds)
            session.add(user_credentials)

            # Make RPC to Users service to create a user object

            # Return an access token and refresh token


            

        except:
            session.rollback()
        else:
            session.commit()


@auth.route('/oauth2/google/token', methods=['POST'])
def refresh_token():
    data: dict = request.get_json()

    refresh_token = data.get('refresh_token')


@auth.route('/', methods=['GET'])
def index():
    return '<a href="/login">Login with Google</a>'

# /login/google


@auth.route('/login/google')
def login_with_google():
    redirect_uri = url_for('auth.authorize_google', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

# revoke endpoint


@auth.route('/authorize/google')
def authorize_google():
    token = oauth.google.authorize_access_token()
    print(token)

    # email = session.get()

    return token
