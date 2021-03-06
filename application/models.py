from application.app import app, db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))

class Weight(db.Model):
    entry_id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    e_date = db.Column(db.Date, default = datetime.datetime.today, nullable= False)
    e_weight = db.Column(db.Float, nullable = False)

# Sample for One-many and Many-Many relationship
# class WorkItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(120))

#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     shared_with = db.relationship('User', secondary=shared_with, lazy='subquery', backref=db.backref('user', lazy=True))

# shared_with = db.Table('shared_with',
#     db.Column('work_item_id', db.Integer, db.ForeignKey('work_item.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

# Using the above sample write the DB models here



# create all tables and initialize app

db.create_all()
db.init_app(app)