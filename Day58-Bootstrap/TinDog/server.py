# Udemy: Master Python by building 100 projects in 100 days
# Feb 15, 2025
# Day 58 - TinDog
# A clone version of https://appbrewery.github.io/tindog/
# Created by me

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
