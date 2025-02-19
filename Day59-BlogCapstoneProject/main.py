# Feb 19, 2025
# Day 58 - Blog Capstone Project
# Add upgrade to existing blog template
# Created by me

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
