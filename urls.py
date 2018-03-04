import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

#setting a template directory
template_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(template_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

#setting up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/SampleSearchApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120),  nullable=False)
    firstName = db.Column(db.String(120))
    lastName = db.Column(db.String(120))

    def __init__(self, email, password, firstName, lastName):
    	self.email = email
    	self.password = password
    	self.firstName = firstName
    	self.lastName = lastName

    def __repr__(self):
        return '<User %r>' % self.firstName + ' ' + self.lastName

@app.route("/", methods=['GET'])
def home():
	return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html', my_string="Hello World!")
	else:
		print request.form['username']
		print request.form['password']
		return "Hello World"

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	else:
		print request.form['firstname']
		print request.form['lastname']
		print request.form['email']
		print request.form['password']
		return "Hello World!"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
	db.create_all()
	admin = User('abc@asu.edu', 'apoorv', 'Apoorv', 'Khairnar')
	db.session.add(admin)
	db.session.commit()
	app.run(debug=False)
