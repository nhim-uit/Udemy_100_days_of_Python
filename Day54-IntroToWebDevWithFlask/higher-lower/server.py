# Udemy: Master Python by building 100 projects in 100 days
# Feb 10, 2025
# Day 54 - Introduction to Web Development with Flask
# Higher or lower game utilizing Flask
# Created by me (Alex Mai)

import random
from flask import Flask

app = Flask(__name__)

random_number = random.randint(1, 9)
print(random_number)


@app.route('/')
def welcome():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route('/<int:number>')
def compare(number):
    if number < random_number:
        return ('<h1 style="color:blue">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    elif number > random_number:
        return ('<h1 style="color:red">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    else:
        return (f'<h1 style="color:green">You found the right number, it\'s {random_number}</h1>'
                f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__=='__main__':
    app.run(debug=True)
