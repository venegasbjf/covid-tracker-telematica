from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcrud'

mysql = MySQL()

# Routes Definition
@app.route('/')
def Index():
    return 'Hello World'

@app.route('/add_user')
def add_user():
    return 'User Added'

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)