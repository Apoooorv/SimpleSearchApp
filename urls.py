import os
from flask import Flask, render_template

template_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(template_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def hello():
	return render_template('login.html')

if __name__ == '__main__':
	app.run(debug=False)
