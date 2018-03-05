from app import app, db
from flask import render_template, url_for, redirect, request
from flask_login import current_user, login_user, logout_user
from app.models import User
from sqlalchemy.exc import IntegrityError
from elastic import searchQuery

@app.route("/", methods=['GET'])
def home():
	return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('dashboard'))
	if request.method == 'GET':
		return render_template('login.html')
	if request.form['submit'] == 'Register':
		return redirect(url_for('register'))
	else:
		user = User.query.filter_by(username=request.form['username']).first()
		if user is None or not user.check_password(request.form['password']):
			return render_template('login.html', error='Invalid email or password')
		login_user(user, remember=request.form['remember_me'])
		return redirect(url_for('dashboard'))

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	else:
		username = request.form['username']
		firstName = request.form['firstname']
		lastName = request.form['lastname']
		email = request.form['email']
		password = request.form['password']
		confirm_password = request.form['confirm_password']

		if password != confirm_password:
			return render_template('register.html', error='Passwords do not match!')

		try:
			user = User(username= username, first_name=firstName, last_name=lastName, email=email, password=password)
			db.session.add(user)
			db.session.commit()
		except IntegrityError as e:
			return render_template('register.html', error='Username already exists')
		except Exception as e:
			return render_template('register.html', error=e.message)

		return redirect(url_for('login'))


@app.route("/dashboard", methods=['GET'])
def dashboard():
	return render_template('dashboard.html', user=current_user)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/search', methods=['GET'])
def search():
	if current_user.is_authenticated:
		query = request.args.get('query')
		response = searchQuery(query)
		return render_template('dashboard.html', user=current_user, results=response, query=query)
	return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404