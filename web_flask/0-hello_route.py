#!/usr/bin/python3
"""start a flask application on default parameters"""
from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_world():
    """display a string"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(port=5000)
