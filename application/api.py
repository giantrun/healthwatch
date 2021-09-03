from flask import request
from flask.wrappers import Request
from application.app import app

# Import your models here
from application.models import User, Weight

@app.route("/")
def home():
    return {"Status": "Success"}, 200 

# Write your API endpoints here
# Register User - /user/register
# Login User - /user/login
# Update weight for a date - /weight
# List weight for a date range - /weight
# Logout - user/logout

# 1. List all users
@app.route("/user")
def list_user():
    return {"Status": "Success",
            "data": {
                "User" : "username"
            }}, 200 

# 2. Add users
@app.route("/user", methods = ["POST"])
def add_user():
    return {"Status": "Success",
            "data": {
                "User" : "username",
                "Password" : "password"
            }}, 200 

# 3. Add weight entry
@app.route("/weight", methods = ["POST"])
def add_weight():
    return {"Status": "Success",
            "data": {
                "Userid" : "userid"
            }}, 200 
# 4. List all weight entries