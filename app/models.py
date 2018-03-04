from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(120))
    password_hash = db.Column(db.String(256))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    def __init__(self, username, first_name, last_name, email, password):
    	self.username = username
    	self.email = email
    	self.first_name = first_name
    	self.last_name = last_name
    	self.password_hash = self.set_password(password)

    def __repr__(self):
        return (self.first_name + ' ' + self.last_name)

    def check_password(self, password):
   		return check_password_hash(self.password_hash, password)

    def set_password(self, password):
    	return generate_password_hash(password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))