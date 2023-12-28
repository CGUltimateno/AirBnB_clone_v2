#!/usr/bin/python3
""""
script that starts a Flask web application with the following conditions:
- listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """display HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host="0")
