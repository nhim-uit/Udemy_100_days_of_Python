# Udemy: Master Python by building 100 projects in 100 days
# Feb 19-23, 2025
# Day 59 - Blog Capstone Project
# Add upgrade to existing blog template
# Created by me

import smtplib
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()
my_email = 'alex.test.app.7@gmail.com'
my_password = os.getenv('EMAIL_PASSWORD')


app = Flask(__name__)

response = requests.get('https://api.npoint.io/5ab7588e98376bb9d4dc').json()


@app.route('/')
def home():
    return render_template('index.html',
                           posts=response)


@app.route('/about')
def get_about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def get_contact():
    if request.method == 'POST':
        data = request.form

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='alexisfun065@gmail.com',
                                msg=f'Subject:Hello\n\nThis is {data["name"]}\n'
                                    f'Email: {data["email"]}\n'
                                    f'Phone: {data["phone"]}\n'
                                    f'Message: {data["message"]}.')
        return "<h1>Successfully sent your message</h1>"
    return render_template('contact.html')


@app.route('/post/<id>')
def get_post(id):
    requested_post = None

    for i in response:
        if i['id'] == int(id):
            requested_post = i

    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
