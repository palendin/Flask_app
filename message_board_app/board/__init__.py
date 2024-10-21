# this will create a message board utilizing the following: packaging the files, application factory, and navigation menu
# reference: https://realpython.com/flask-project/#leverage-blueprints
from flask import Flask, render_template, request, redirect, url_for


# start with the flask instance,
# this function is "application factory", allows to flexibility and scaling
def create_app():
    app = Flask(__name__)

    return app


@app.route('/')
def home():
    return "Hello"


if __name__ == "__main__":
    # run flask. If using mac and port already in use, run lsof -i :<port>, kill -9 <PID>
    app.run(debug=True)


