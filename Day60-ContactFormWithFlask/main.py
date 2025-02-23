# Udemy: Master Python by building 100 projects in 100 days
# Feb 19-23, 2025
# Day 60 - Contact Form with POST and Flask

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def receive_data():
    return f"<h1>Email: {request.form['email1']}, password: {request.form['password1']}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
