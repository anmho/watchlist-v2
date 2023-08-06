from flask import jsonify, abort
from src import create_app
from werkzeug.exceptions import HTTPException

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
    app.run(debug=app.config['DEBUG'])
