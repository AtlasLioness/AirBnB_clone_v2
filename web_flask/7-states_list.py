#!/usr/bin/python3
"""
Module that starts a Flask web app.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Displays HTML page with states listed in a-z order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """removes SQLAlchemy session after request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
