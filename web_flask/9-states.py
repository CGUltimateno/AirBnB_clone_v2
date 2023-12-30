#!/usr/bin/python3
"""
Define a module to serve requests for
states.
"""
from models.state import State
from models.state import City
from models import storage
from os import environ
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states")
def states():
    """ Retrieve a list of all states. """
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
def destroy(obj):
    storage.close()


if __name__ == '__main__':
    app.run(host='0')
