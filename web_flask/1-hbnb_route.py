#!/usr/bin/python3
"""
start Flask application
"""
from flask import Flask
app = Flask(__name__)


# Define routes
@app.route('/', strict_slashes=False)
def index():
    """Return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
