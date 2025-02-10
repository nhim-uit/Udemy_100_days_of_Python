# Udemy: Master Python by building 100 projects in 100 days
# Feb 08, 2025
# Day 54 - Introduction to Web Development with Flask

from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper_function():
        return '<b>' + func() + '</b>'

    return wrapper_function


def make_emphasis(func):
    def wrapper_function():
        return '<em>' + func() + '</em>'

    return wrapper_function


@app.route('/')     # decorator
def hello_world():
    return '<h1 style="text-align: center">Hello, World</h1>' \
           '<p>This is a paragraph.</p>'


@app.route('/bye')
@make_bold
@make_emphasis
def say_bye():
    # return '<u><em><b>Bye</b></em></u>'
    return 'Bye'


@app.route('/hello/<name>/<int:number>')
def hello_name(name, number):
    return f'Hello {name}, you are {number} years old!'
# /hello/<path:name>
# /hello/<name>/<int:number>


if __name__ == '__main__':
    # run the app in debug mode for auto reloading
    app.run(debug=True)

