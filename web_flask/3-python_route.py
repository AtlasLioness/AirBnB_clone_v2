#!/usr/bin/python3
"""
Module that starts a flask web app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' at the root route."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB' at the /hbnb route."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def croute(text):
    """display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space"""
    return "C " + text.replace('_', ' ')


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonroute(text):
    """display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space"""
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
