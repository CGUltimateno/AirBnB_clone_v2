#!/usr/bin/python3
"""
Define a module to serve requests
for states.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states')
def states():
    """Display a HTML page with a list of states."""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    """Display a HTML page with a list of states."""
    states = storage.all(State)
    dict = {}
    state = ""
    for key, value in states.items():
        if value.id == id:
            dict[key] = value.cities
            state = value.name
            break

    return (render_template("9-states.html",
                            states=dict, id=id, state=state))

@app.teardown_appcontext
def teardown_db(exception):
    """Close the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0')
