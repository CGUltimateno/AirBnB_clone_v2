#!/usr/bin/python3
"""
script that starts a Flask web application with routes /, /hbnb, /c/<text>,
/python<text>, and /number/<n>, /number_template/<n>, and /number_odd_or_even/<n>.
"""
from flask import Flask, abort, render_template

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


@app.route('/python/<text>')
def python(text):
    """display Python followed by text"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/python/')
def python_default():
    """display Python followed by text"""
    return 'Python is cool'


@app.route("/number/<num>")
def number(num):
    """display n is a number only if n is an integer"""
    if num.isdigit():
        return f"{int(num)} is a number"

    abort(404)


@app.route("/number_template/<num>")
def number_template(num):
    """display a HTML page only if n is an integer"""
    if num.isdigit():
        return render_template("5-number.html", num=num)

    abort(404)


@app.route("/number_odd_or_even/<num>")
def number_odd_or_even(num):
    """display a HTML page only if n is an integer"""
    if num.isdigit():
        return render_template("6-number_odd_or_even.html", num=num)

    abort(404)


if __name__ == "__main__":
    app.run(host="0")
