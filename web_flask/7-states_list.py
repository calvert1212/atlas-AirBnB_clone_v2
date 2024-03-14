#!/usr/bin/python3
""" Starts a Flask web application """

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page with list of all State objects in DBStorage by name"""
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_storage(exception):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
