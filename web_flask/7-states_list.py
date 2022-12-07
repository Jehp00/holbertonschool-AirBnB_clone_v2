#!/usr/bin/python3
"""
Module list states on index
"""

from flask import Flask, render_template
from models import storage


"""object flask"""
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """close the session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """list states in html file"""
    states_obj = [s for s in storage.all("State").values()]
    return render_template("7-states_list.html", states_obj=states_obj)


if __name__ == '__main__':
    """run the app flask"""
    app.run(host='0.0.0.0', port=5000, debug=True)
