#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """ Displays an AirBnB clone filter page """

    # Load states, cities, and amenities from the database and sort them
    states = sorted(list(storage.all('State').values()), key=lambda s: s.name)
    cities = sorted(list(storage.all('City').values()), key=lambda c: c.name)
    amenities = sorted(list(storage.all('Amenity').values()),
                       key=lambda a: a.name)

    # Pass data to template and render
    return render_template('10-hbnb_filters.html',
                           states=states,
                           cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def close_storage(self):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
