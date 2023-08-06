import base64
import binascii
from typing import Dict, Tuple
import jwt
from datetime import datetime, timedelta
from src.config import Config


def parse_basic_auth(auth: str) -> Tuple[str]:
    # Ensure auth is a string
    if not isinstance(auth, str):
        raise TypeError("auth parameter must be a string")

    # Ensure auth is Basic auth
    if not auth.startswith("Basic"):
        raise ValueError("Auth must be Basic")

    pieces = auth.split(" ")
    # Ensure auth contains username and password
    if len(pieces) < 2:
        raise ValueError("Basic Auth must contain credentials")
    elif len(pieces) > 2:
        raise ValueError("Basic Auth contains too many components")

    encoded_creds = pieces[1]
    username, password = None, None
    # Ensure in base64
    try:
        encoded_creds = base64.b64decode(
            encoded_creds, validate=True).decode("utf-8")
    except binascii.Error:
        raise ValueError("Auth is invalid base64 string")

    creds = encoded_creds.split(":")
    if len(creds) < 2:
        raise ValueError("Auth must provide username and password")
    elif len(creds) > 2:
        raise ValueError("Auth contains too many components")

    email, password = creds

    if not email or not password:
        raise ValueError("Auth must contain email and password")

    return (email, password)


def create_credentials(email: str, password):
    pass
