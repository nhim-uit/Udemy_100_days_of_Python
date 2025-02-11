# Udemy: Master Python by building 100 projects in 100 days
# Feb 11, 2025
# Day 57 - Age and gender guessing using API agify and genderize, Flask, Jinja
# Created by me (Alex Mai)

from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/<name>')
def get_results(name):
    agify_res = requests.get(f'https://api.agify.io?name={name}').json()
    age = agify_res['age']
    print(agify_res, age)

    return render_template('index.html', name=name.title(), gender=gender, age=age)



