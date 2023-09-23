#!/usr/bin/python3
"""start a flask application with a route HBNB"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """display a string"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """display HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run()
