# Feb 19-23, 2025
# Day 58 - Blog Capstone Project
# Add upgrade to existing blog template
# Created by me

import requests
from flask import Flask, render_template

app = Flask(__name__)

response = requests.get('https://api.npoint.io/5ab7588e98376bb9d4dc').json()

@app.route('/')
def home():
    return render_template('index.html',
                           posts=response)


@app.route('/about')
def get_about():
    return render_template('about.html')


@app.route('/contact')
def get_contact():
    return render_template('contact.html')


@app.route('/post/<id>')
def get_post(id):
    return render_template('post.html', post=response[int(id) - 1])


if __name__ == '__main__':
    app.run(debug=True)
