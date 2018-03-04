from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    def __init__(self, first_name, last_name, email, password):
    	self.email = email
    	self.first_name = first_name
    	self.last_name = last_name
    	self.password_hash = self.set_password(password)

    def __repr__(self):
        return '<User {}>'.format(self.first_name + ' ' + self.last_name)

    def set_password(self, password):
    	self.password_hash = generate_password_hash(password)

   	def check_password(self, password):
        return check_password_hash(self.password_hash, password)
