from flask import jsonify, abort
from werkzeug.exceptions import HTTPException

from src import create_app

app = create_app()


@app.errorhandler(Exception)
def handle_error(e: Exception):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code

    response = {
        "msg": e.description or "Something went wrong",
        **(e.response or {})
    }

    return response, code


if __name__ == "__main__":
    # app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000)
