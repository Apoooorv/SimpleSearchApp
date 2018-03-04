import os
from flask import Flask, render_template, redirect, url_for, request

template_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(template_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

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
	app.run(debug=False)
