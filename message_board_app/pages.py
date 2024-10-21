# As your Flask project grows, you have lots of view functions and other related bits of code that work together. 
# Instead of adding all these directly to a basic app.py file, you can create blueprints that you register in your application factory
from flask import Blueprint

# blueprints are existing view functions
bp = Blueprint("pages", __name__)

# using the view functions to the route
@bp.route("/")
def home():
    return "Hello, Home!"

@bp.route("/about")
def about():
    return "Hello, About!"