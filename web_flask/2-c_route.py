#!/usr/bin/python3
"""application with flask framework"""
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


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """use given text"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
