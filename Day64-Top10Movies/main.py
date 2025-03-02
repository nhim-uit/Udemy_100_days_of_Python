# Udemy: Master Python by building 100 projects in 100 days
# Mar 02, 2025
# Day 64 - My Top 10 Movies
# Created by me (Alex Mai)

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
