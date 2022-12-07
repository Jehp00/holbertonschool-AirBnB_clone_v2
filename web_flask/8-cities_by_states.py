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
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown(exc):
    """close the session"""
    storage.close()

@app.route('/cities_by_states')
def cities_by_states():
    """display html page
       fetch sorted states to insert into html in UL tag
       fetch sorted cities in each state into LI tag ->in HTML file
    """
    cities_and_states = [sc for sc in storage.all("State").values()]
    return render_template('8-cities_by_states.html',
                           state_objs=state_objs)


if _name_ == '_main_':
    """run the app flask"""
    app.run(host='0.0.0.0', port=5000, debug=True)