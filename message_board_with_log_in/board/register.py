from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session
from .models import User
from .extensions import db

bp = Blueprint("registration", __name__)

# Dummy user credentials for login
users = {
    "admin": "admin",  # Admin credentials
    "guest": "guest"   # Guest credentials
}

# user registration. The submit button in the registration form triggers the same register() function. This function handles both the initial display of the registration form (GET request) and the processing of the form submission (POST request).
@bp.route("/register", methods=['GET', 'POST'])
def register():
    # if 'username' not in session:
    #     return redirect(url_for('pages.login')) 
    
    if request.method == "POST":
        # get data from form
        username = request.form["username"]
        password = request.form["password"] 

        # Check if the user already exists by querying the database
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Please choose a different username.", category="error")

        if username and password:
            # create a new user instance
            user = User(username=username, password=password)
            
            # Add and commit the new post to the database
            db.session.add(user)
            db.session.commit()

            flash("Thanks for registering!", category="success") 
            return redirect(url_for("pages.home"))

        else:
            # display error message
            flash("username and password are required!", category="error")

    return render_template("pages/register.html")