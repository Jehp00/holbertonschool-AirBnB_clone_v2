#!/usr/bin/python3
"""
Module route to C <text> with Flask
"""
from flask import Flask, render_template


"""declaring the app with the Flask class"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index to web to print a messege running the host and port
    on the web address (URL)"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route to web to print a messege running the host and port
    on the web second address (URL)"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """route to page c is something, using the variable text we
    can change the text and the URL anytime"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """route to page python is something, using the variable text we
    can change the text and the URL anytime"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_n(n):
    """return a number if th parameter is a number with a messege"""
    return "{} is a number".format(int(n))


@app.route('/number_template/<int:n>')
def num_templeates(n):
    """return an index.html if n is a number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    """running the app"""
    app.run(host='0.0.0.0', port=5000, debug=True)
