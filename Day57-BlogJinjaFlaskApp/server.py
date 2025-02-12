# Udemy: Master Python by building 100 projects in 100 days
# Feb 11-12, 2025
# Day 57 - Templating with Jinja in Flask Application
# multiline statements with Jinja
# agify API, genderize API
# npoint API

from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template('index.html', num=random_num, year=year)


@app.route('/<name>')
def get_results(name):
    agify_res = requests.get(f'https://api.agify.io?name={name}').json()
    age = agify_res['age']

    genderize_res = requests.get(f'https://api.genderize.io?name={name}').json()
    gender = genderize_res['gender']

    return render_template('guess.html', name=name.title(), gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'

    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)

