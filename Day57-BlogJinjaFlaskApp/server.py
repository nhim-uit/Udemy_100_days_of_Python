# Udemy: Master Python by building 100 projects in 100 days
# Feb 11, 2025
# Day 57 - Templating with Jinja in Flask Application

from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template('index.html', num=random_num, year=year)


if __name__ == '__main__':
    app.run(debug=True)

