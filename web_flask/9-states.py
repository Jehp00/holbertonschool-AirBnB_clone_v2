#!/usr/bin/python3
"""
script starts Flask web app
"""
from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(exc):
    """after each request remove current SQLAlchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    """list states in html file"""
    states_obj = [s for s in storage.all("State").values()]
    return render_template("7-states_list.html", states_obj=states_obj)


@app.route('/cities_by_states')
def cities_by_states():
    """
       fetch sorted states to insert into html in UL tag
    """
    state_objs = [s for s in storage.all("State").values()]
    return render_template('8-cities_by_states.html',
                           state_objs=state_objs)


@app.route('/states/<id>')
def states_id(id):
    """fetch sorted states with its id's to insert into html in UL"""
    states = None
    for state in storage.all("State").values():
        if state.id == id:
            states = state
    return render_template("9-states.html", states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
