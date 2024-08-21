#!/usr/bin/python3
"""
Module that starts a Flask web app.
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exc):
    """removes SQLAlchemy session after request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays HTML page with states listed in a-z order"""

    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
