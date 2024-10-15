from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Creating the Flask app object, called WSGI (Web Server Gateway Interface). A WSGI (Web Server Gateway Interface) is a standard that defines how web servers and web applications communicate with each other.
app = Flask(__name__) #  file named app.py, then __name__ will be app.py. Flask will then look for templates in a folder named templates and static files in a folder named static, both located within the same directory as app.py.

# @app.route('/') # route() function of the Flask class is a decorator. When a user visits this URL, the hello_world function is called
# def hello_world():
#    return 'Hello World'

@app.route('/hello')  # if a user visits http://localhost:5000/hello URL, hello_world function will be called
def hello_world():
   return 'Hello World'


if __name__ == '__main__':
   app.run()
