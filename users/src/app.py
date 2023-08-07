from flask import Flask
# REST Server

app = Flask(__name__)

@app.route("/users")
def hello():
    return "hello"

