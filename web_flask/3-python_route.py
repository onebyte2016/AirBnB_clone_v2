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

@app.route('/c/', strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def show_c(text=""):
    # Replace underscores with spaces in the text
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text="is_cool"):
    # Replace underscores with spaces in the text
    text = text.replace('_', ' ')
    return f"Python {text}"

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
