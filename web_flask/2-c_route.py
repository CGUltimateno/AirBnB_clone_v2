#!/usr/bin/python3
"""
script that starts a Flask web application with routes /, /hbnb and /c/<text>.
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


@app.route('/c/<text>')
def c(text):
    """display C followed by text"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0")
