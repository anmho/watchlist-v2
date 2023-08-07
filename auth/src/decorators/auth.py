import binascii
import logging
from flask import request
from werkzeug.exceptions import Forbidden, BadRequest, InternalServerError


def basic_auth_required(route_function):
    """ 
    Handles Basic Authentication by intercepting the requiest object and verifies it, passing the email credential
    """

    def wrapper():
        if 'Authorization' not in request.headers:
            raise Forbidden('email and password required')  # 403

        try:
            auth = request.headers['Authorization']
            username, password = parse_basic_auth(auth)
        except (TypeError, ValueError, binascii.Error) as e:
            logging.exception(str(e))
            raise BadRequest(str(e)) from e  # 400
        except Exception as e:
            raise InternalServerError(str(e)) from e

        route_function()

    pass


def bearer_auth_required():
    pass
