#!/usr/bin/python3
"""
Module route to C <text>
"""


from flask import Flask


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
    new_text = text.replace('_', ' ')
    return f"C {new_text}"


if __name__ == '__main__':
    """running the app"""
    app.run(host='0.0.0.0', port=5000, debug=True)
