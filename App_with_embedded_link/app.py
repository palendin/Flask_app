from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)

# Secret key for session management (necessary for using sessions)
app.secret_key = 'your_secret_key'

# Dummy user credentials for login
users = {
    "admin": "adminpassword",  # Admin credentials
    "guest": "guestpassword"   # Guest credentials
}

# Set session lifetime to 30 minutes
app.permanent_session_lifetime = timedelta(minutes=30)

# automatically redirect users from the root URL (/) to the login page when opening the app:
@app.route('/')
def home():
    return redirect(url_for('login'))

# Guest greeting route
@app.route('/guest/<guest>')
def hello_guest(guest):
    if 'username' in session and session['username'] == guest: # Data stored in session is kept for the duration of the user's session
        return f'Hello {guest}, you are a guest'
    else:
        return redirect(url_for('login'))  # Redirect to login if not logged in

# Admin greeting route
@app.route('/admin')
def hello_admin():
    if 'username' in session and session['username'] == 'admin': # Data stored in session is kept for the duration of the user's session
        return 'Hello Admin'
    else:
        return redirect(url_for('login'))  # Redirect to login if not logged in

# Login route (for handling login form submissions)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate credentials
        if username in users and users[username] == password: # users is a dictionary, username is key and password is value (example users = {'admin': 'admin_password', 'guest': 'guest_password'})
            session['username'] = username  # Store the username in session. Data stored in session is kept for the duration of the user's session
            session.permanent = True  # Make the session permanent
            if username == 'admin':
                return redirect(url_for('hello_admin'))
            else:
                return redirect(url_for('hello_guest', guest=username))
        else:
            return 'Invalid credentials. Please try again.'
    return render_template('login.html')  # Renders the login form

# Logout route to clear the session
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session. Session object is used to store data across requests for a particular user. Data stored in session is kept for the duration of the user's session, which is typically until they close the browser or log out.
    return redirect(url_for('login'))

# Additional route after login (e.g., user dashboard)
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return f'Welcome to your dashboard, {username}!'
    else:
        return redirect(url_for('login'))  # Redirect to login if not logged in

if __name__ == '__main__':
    app.run(debug=True)