# blueprint for posting messages

# As your Flask project grows, you have lots of view functions and other related bits of code that work together. 
# Instead of adding all these directly to a basic app.py file, you can create blueprints that you register in your application factory
from flask import Blueprint, render_template

# blueprints are existing view functions
bp = Blueprint('posts', __name__)


@bp.route("/create")
def create():
    # contact_info.html leads to a separate page
    return render_template("posts.create.html")

