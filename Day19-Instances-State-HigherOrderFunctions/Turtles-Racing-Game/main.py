# Udemy: Master Python by building 100 projects in 100 days
# Aug 27, 2024
# Day 19 - Turtles Racing Game
# Created by me: using oop - encapsulation

from turtle import Screen
from Turtles import *
from functions import choose_color

if __name__ == '__main__':
    # create screen
    screen = Screen()
    screen.setup(width=500, height=400)

    # prompt to ask for user's color
    user_color = choose_color(screen)

    # create turtles
    my_turtles = Turtles()
    my_turtles.create()

    # start racing
    my_turtles.race(user_color)

    # exit screen on click
    screen.exitonclick()
