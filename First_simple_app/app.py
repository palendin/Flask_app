from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Creating the Flask app object, called WSGI (Web Server Gateway Interface). A WSGI (Web Server Gateway Interface) is a standard that defines how web servers and web applications communicate with each other.
app = Flask(__name__) #  file named app.py, then __name__ will be app.py. Flask will then look for templates in a folder named templates and static files in a folder named static, both located within the same directory as app.py.

# @app.route('/') # route() function of the Flask class is a decorator. When a user visits this URL, the hello_world function is called
# def hello_world():
#    return 'Hello World'

# @app.route('/hello')  # if a user visits http://localhost:5000/hello URL, hello_world function will be called
# def hello_world():
#    return 'Hello World'

# dynamic URL
@app.route('/test/<name>') # user can enter any name at the end of the URL (http://localhost:5000/hello) and it will be passed to the hello_name function
def hello_name(name):
   return 'Test Hello %s!' % name

# can add more routes
@app.route('/') # route() function of the Flask class is a decorator. When a user visits this URL, the hello_world function is called
def hello_world():
   return 'Hello World'

@app.route('/python')  # if a user visits http://localhost:5000/python URL, hello_python function will be called
def hello_python():
   return 'Hello python'

@app.route('/guest/<guest>') 
def hello_guest(guest):
   return f'Hello {guest}, you are a guest'

@app.route('/admin')
def hello_admin():
    return 'hello admin'

# when user enters any name, it will redirect to another URL
@app.route('/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin')) 
   else:
      return redirect(url_for('hello_guest',guest = name))
   

if __name__ == '__main__':
   app.run()
