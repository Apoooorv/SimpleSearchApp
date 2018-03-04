from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')


class RegisterForm(FlaskForm):
	firstName = StringField('FirstName')
	lastName = StringField('LastName')
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[
		DataRequired(),
		EqualTo('confirm', message='Passwords must match')
	])
	confirm = PasswordField('Repeat Password')
	submit = SubmitField('Register')