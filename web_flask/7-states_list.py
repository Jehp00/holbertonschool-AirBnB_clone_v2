#!/usr/bin/python3
"""
Module list states on index
"""

from flask import Flask, render_tamplate
from models import storage


"""object flask"""
app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """list states in html file"""
    new_states = storage.all(State)
    return render_tamplate("7-states_list.html", new_states=new_states)


@app.teardown_appcontext
def teardown(exc):
    """close the session"""
    storage.close()


if __name__ == '__main__':
    """run the app flask"""
    app.run(debug=True, host='0.0.0.0', port=5000)