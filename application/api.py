from flask import request
from flask.wrappers import Request
from application.app import app
from flask_jwt import jwt_required, JWT, current_identity

# Import your models here
from application.models import User, Weight, db
from datetime import datetime

@app.route("/")
def home():
    return {"Status": "Success"}, 200 

# Write your API endpoints here
# Register User - /user/register
# Login User - /user/login
# Update weight for a date - /weight
# List weight for a date range - /weight
# Logout - user/logout




# def identity(payload):
#     user_id = payload['identity']
#     return User.query.filter_by(id=user_id).first()

# def authenticate(username, password):
#     user = User.query.filter_by(username=username).first()
#     if user and user.password == password:
#         return user

# jwt = JWT(app, authenticate, identity)

# @app.route("/hello")
# @jwt_required()
# def hello_world():
#     return {"Status": "Success", "result": f"Hello {current_identity.username}"}

# 1. List all users
@app.route("/user")
def list_user():
    users = User.query.all()

    results = []
    for user in users:
        results.append({
            "User id": user.id,
            "user name": user.username
        })
    return {"Status": "Success", "data": results}, 200

# 2. Add users
@app.route("/user", methods = ["POST"])
def add_user():
    params = request.json
    print (params)
    user1 = User(username=params["username"], password=params["password"])
    db.session.add(user1)
    db.session.commit()
    return {"Status": "User added successfully",
            "data": {
                "User" : user1.username
            }}, 200 


# 3. Add weight entry
@app.route("/weight", methods = ["POST"])
def add_weight():
    params = request.json
    print (params)
    weight1 = Weight(userid=params["userid"], e_weight=params["e_weight"])
    db.session.add(weight1)
    db.session.commit()
    return {"Status": "Weight added successfully",
            "data": {
                "Userid" : weight1.userid,
                "weight entry" : weight1.e_weight
            }}, 200 


# 4. List all weight entries
@app.route("/weight", methods = ["GET"])
def list_all_weights():
    # Read what is being returned
    weights = Weight.query.all()

    results = []
    for weight in weights:
        results.append({
            "weight_id": weight.entry_id,
            "userid": weight.userid,
            "e_weight": weight.e_weight,
            "date": weight.e_date
        })
    return {"Status": "Success", "data": results}, 200

# 5. Add weight entry for a given date
@app.route("/weight_date", methods = ["POST"])
def add_weight_date():
    params = request.json
    print (params)
    weight1 = Weight(userid=params["userid"], e_date=datetime.strptime((params["e_date"]),'%d/%m/%y'), e_weight=params["e_weight"])
    db.session.add(weight1)
    db.session.commit()
    return {"Status": "Weight added successfully",
            "data": {
                "Userid" : weight1.userid,
                "Date" : weight1.e_date,
                "weight entry" : weight1.e_weight
            }}, 200 

# 6. List all weight entries for a given user
@app.route("/weight_given_id", methods = ["POST"])
def list_weights_for_date():
    params = request.json
    print (params)
    weights = Weight.query.filter(Weight.userid == params["userid"])

    results = []
    for weight in weights:
        results.append({
            "weight_id": weight.entry_id,
            "userid": weight.userid,
            "e_weight": weight.e_weight,
            "date": weight.e_date
        })
    return {"Status": "Success", "data": results}, 200

# def create_users():
#     user1 = User(username='user1', password='123')
#     user2 = User(username='user2', password='123')
#     user3 = User(username='user3', password='123')

#     db.session.add(user1)
#     db.session.add(user2)
#     db.session.add(user3)
#     db.session.commit()

# def create_work_item():
#     user1 = User.query.filter_by(username="user1").first()
#     user2 = User.query.filter_by(username="user2").first()
#     work_item = WorkItem(title='work item 1', description='description 1', created_by=user1.id, shared_with=[user2])
#     db.session.add(user1)
#     db.session.commit()