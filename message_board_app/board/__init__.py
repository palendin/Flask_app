# this will create a message board utilizing the following concept: application factory, blueprint, view functions (navigation menu)
# reference: https://realpython.com/flask-project/#leverage-blueprints
from flask import Flask, render_template, request, redirect, url_for
from board import pages

# start with the flask instance,
# this function is "application factory", allows to flexibility and scaling
def create_app():
    app = Flask(__name__)

    # connect view function in pages.py to Flask app
    app.register_blueprint(pages.bp)

    return app





