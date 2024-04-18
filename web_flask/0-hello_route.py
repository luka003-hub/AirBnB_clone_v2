#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask
app = Flask(app)


@app.route('/airbnb-onepage/')
def hello():
    return "Hello, Airbnb One Page!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

