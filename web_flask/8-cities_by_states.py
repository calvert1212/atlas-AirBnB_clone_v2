#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """ Displays a HTML page with a list of all states and their cities """
    states = storage.all(State)
    sorted_states_list = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html',
                           states=sorted_states_list)


@app.teardown_appcontext
def close_session(exception):
    """ Closes the session after each request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
