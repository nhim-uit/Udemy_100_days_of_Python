# Feb 19, 2025
# Day 58 - Blog Capstone Project
# Add upgrade to existing blog template
# Created by me

import requests
from flask import Flask, render_template
from streamlit import title

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/5ab7588e98376bb9d4dc').json()
    titles = []
    subtitles = []
    authors = []
    dates = []

    for i in response:
        titles.append(i['title'])
        subtitles.append(i['subtitle'])
        authors.append(i['author'])
        dates.append(i['date'])

    length = len(titles)

    return render_template('index.html',
                           titles=titles,
                           subtitles=subtitles,
                           authors=authors,
                           dates=dates,
                           length=length)


@app.route('/about')
def get_about():
    return render_template('about.html')


@app.route('/contact')
def get_contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
