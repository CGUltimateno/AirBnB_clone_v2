#!/usr/bin/python3
"""
Define a module to serve requests
for cities.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """Display a HTML page with a list of states."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """Display a HTML page with a list of states."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0')
