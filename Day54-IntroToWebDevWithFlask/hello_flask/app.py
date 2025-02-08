# Udemy: Master Python by building 100 projects in 100 days
# Feb 08, 2025
# Day 54 - Introduction to Web Development with Flask

from flask import Flask

app = Flask(__name__)


@app.route('/')     # decorator
def hello_world():
    return 'Hello, World'


@app.route('/bye')
def say_bye():
    return 'Bye'


@app.route('/hello/<name>/<int:number>')
def hello_name(name, number):
    return f'Hello {name}, you are {number} years old!'
# /hello/<path:name>
# /hello/<name>/<int:number>


if __name__ == '__main__':
    # run the app in debug mode for auto reloading
    app.run(debug=True)

