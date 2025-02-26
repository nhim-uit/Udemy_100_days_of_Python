# Udemy: Master Python by building 100 projects in 100 days
# Feb 26, 2025
# Day 61 - Advanced form with WTForms (Flask)

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'asdf213'


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
