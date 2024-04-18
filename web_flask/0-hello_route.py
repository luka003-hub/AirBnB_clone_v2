#!/usr/bin/python3
"""
A simple Flask web application
"""

from flask import Flask

# Create the Flask application instance named 'app'
app = Flask(__name__)

# Define the route and corresponding function
@app.route('/airbnb-onepage/')
def hello():
    return "Hello, Airbnb One Page!"

# Run the Flask application if executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

