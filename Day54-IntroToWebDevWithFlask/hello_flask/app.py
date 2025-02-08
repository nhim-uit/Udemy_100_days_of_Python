# Udemy: Master Python by building 100 projects in 100 days
# Feb 08, 2025
# Day 54 - Introduction to Web Development with Flask

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'
