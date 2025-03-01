# Udemy: Master Python by building 100 projects in 100 days
# Feb 26 - Mar 01, 2025
# Day 61 - Advanced form with WTForms (Flask)

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = 'asdf213'

bootstrap = Bootstrap5(app)


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In', validators=[DataRequired('Submit credentials')])


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if request.form['email'] == 'abc@gmail.com':
            if request.form['password'] == '12345678':
                return redirect(url_for('success'))
        return redirect(url_for('denied'))

    return render_template('login.html', form=login_form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
