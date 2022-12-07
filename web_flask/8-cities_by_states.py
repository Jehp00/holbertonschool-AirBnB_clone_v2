#!/usr/bin/python3
"""
Module list states on index
"""

from flask import Flask, render_template
from models import storage
from os import getenv
from sqlalchemy.orm import relationship
"""object flask"""
app = Flask(_name_)


@app.teardown_appcontext
def teardown(exc):
    """close the session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes = False)
def cities_by_states():
    """
       fetch sorted states to insert into html in UL tag
    """
    cities_and_states = [sc for sc in storage.all("State").values()]
    return render_template('8-cities_by_states.html',
                           cities_and_states=cities_and_states)


if _name_ == '_main_':
    """run the app flask"""
    app.run(host='0.0.0.0', port=5000, debug=True)