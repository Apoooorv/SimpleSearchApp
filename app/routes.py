from app import app
from flask import render_template, url_for, redirect, request

@app.route("/", methods=['GET'])
def home():
	return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		print request.form['username']
		print request.form['password']
		return "Hello World"

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	else:
		firstName = request.form['firstname']
		lastName = request.form['lastname']
		email = request.form['email']
		password = request.form['password']

		
		


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404