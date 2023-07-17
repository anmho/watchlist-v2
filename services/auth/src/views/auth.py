from werkzeug.exceptions import NotFound, BadRequest, Forbidden
import binascii
from flask import Blueprint, session, redirect, request, url_for, abort, jsonify
from requests import codes
import logging
from src.utils.auth_utils import parse_basic_auth
from src.app import oauth
from src.config import Config
import logging
import requests
from pprint import pprint
from src.config import Config
from requests import PreparedRequest, Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from src.utils.oauth2utils import GoogleOAuth2Manager
from authlib.integrations.requests_client import OAuth2Session
import base64
import traceback

auth = Blueprint('auth', __name__)


retries = Retry(
    total=5,
    backoff_factor=0.1,
    status_forcelist=[502,503, 504],
    allowed_methods={'POST'}
)
sess = Session()
adapter = HTTPAdapter(max_retries=retries)
sess.mount('https://', adapter)
sess.mount('http://', adapter)


# @basic_auth_required
@auth.route('/login', methods=['POST'])
def login():
    """
    Validates user credentials (username + password) and returns a JWT access_token and refresh_token
    """
    if 'Authorization' not in request.headers:
        raise Forbidden('username and password required') # 403
    
    try:
        auth = request.headers['Authorization']
        username, password = parse_basic_auth(auth)
    except (TypeError, ValueError, binascii.Error) as e:
        logging.exception(str(e))
        raise BadRequest(str(e)) from e # 400
    
    # fetch_tokens

    # set this tokens in httponly cookies
    
    return jsonify([username, password]), 200


@auth.route('/signup', methods=['POST'])
def sign_up():

    """
    1) Check that for valid username and password (alongside client checking)
    1) Create a new user
    3) Generate an access token and refresh token for the user
    4) Handle login redirection on client side
    """
    
    return 'New user created'

# @auth.route('/oauth2/google/token', methods=['POST'])
# def refresh_token():
#     data: dict = request.get_json()

#     refresh_token = data.get('refresh_token')

    
@auth.route('/', methods=['GET'])
def index():
    return '<a href="/login">Login with Google</a>'

# /login/google
@auth.route('/login/google')
def login_google():
    redirect_uri = url_for('auth.authorize_google', _external=True)

    return oauth.google.authorize_redirect(redirect_uri)

# revoke endpoint



@auth.route('/authorize/google')
def authorize_google():
    token = oauth.google.authorize_access_token()
    print(token)

    # email = session.get()


    return token
    



    

    # access_token, refresh_token = google_creds_manager.fetch_tokens(code)
    # logging.info(f"Access token and refresh was retrieved {access_token} {refresh_token}")
    # user_info = google_creds_manager.get_user_info(access_token)

    # Process user information
    # email = user_info['email']
    # name = user_info['name']
    # # ... do something with the user data ...
    # # save the tokens

    # session['access_token'] = access_token
    # session['refresh_token'] = refresh_token
    # logging.info(
    #     f'Logging in as user with token {access_token} with data {user_info}')

    # return f'Logged in as {name} ({email})'
