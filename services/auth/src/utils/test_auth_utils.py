import base64
import pytest
from .auth_utils import parse_basic_auth




def test_parse_basic_auth_valid():
    username = "admin"
    password = "admin"
    credentials = f"{username}:{password}"
    creds = base64.b64encode(credentials.encode()).decode("utf-8")
    auth = f"Basic {creds}"
    parsed_username, parsed_password = parse_basic_auth(auth)
    assert parsed_username == username
    assert parsed_password == password

def test_parse_basic_auth_nonstring():
    creds = None
    with pytest.raises(TypeError) as excinfo:
        parse_basic_auth(creds)
    assert str(excinfo.value) == "auth parameter must be a string"

def test_parse_basic_auth_non_basic():
    username = "admin"
    password = "admin"
    credentials = f"{username}:{password}"
    creds = base64.b64encode(credentials.encode()).decode("utf-8")
    auth = f"Bearer {creds}"
    with pytest.raises(ValueError) as excinfo:
        parse_basic_auth(auth)
    assert str(excinfo.value) == "Auth must be Basic"

def test_parse_basic_auth_missing_credentials():
    auth = "Basic"
    with pytest.raises(ValueError) as excinfo:
        parse_basic_auth(auth)
    assert str(excinfo.value) == "Basic Auth must contain credentials"

def test_parse_basic_auth_extra_components():
    username = "admin"
    password = "admin"
    credentials = f"{username}:{password}"
    creds = base64.b64encode(credentials.encode()).decode("utf-8")
    extra_component = "extra"
    auth = f"Basic {creds} {extra_component}"
    with pytest.raises(ValueError) as excinfo:
        parse_basic_auth(auth)
    assert str(excinfo.value) == "Basic Auth contains too many components"

def test_parse_basic_auth_invalid_base64():
    auth = "Basic dXNlcjpwYXNzd29yZA==="
    with pytest.raises(ValueError) as excinfo:
        parse_basic_auth(auth)
    assert str(excinfo.value) == "Auth is invalid base64 string"

def test_parse_basic_auth_missing_username_or_password():
    username = "admin"
    auth = f"Basic {base64.b64encode(username.encode()).decode('utf-8')}"
    with pytest.raises(ValueError) as excinfo:
        parse_basic_auth(auth)
    assert str(excinfo.value) == "Auth must provide username and password"

    password = "admin"
    auth = f"Basic {base64.b64encode(password.encode()).decode('utf-8')}"
    with pytest.raises(ValueError) as excinfo:
        parse_basic_auth(auth)
    assert str(excinfo.value) == "Auth must provide username and password"