#!/usr/bin/python3
"""
Module app route Flask
"""

from flask import Flask


"""declaring the app with the Flask class"""
app=Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """index to web to print a messege running the host and port
    on the web address (URL)"""
    return "Hello HBNB!"

if __name__=='__main__':
    """running the app"""
    app.run(host='0.0.0.0', port=5000, debug=True)