#!/usr/bin/python3
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define routes
@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
