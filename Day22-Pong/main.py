# Udemy: Master Python by building 100 projects in 100 days
# Aug 28 - Sep 6, 2024
# Day 22 - Pong
# Created based on Udemy course
# Modified by me
# Create the screen
# Create paddles
from functions import *
from paddle import Paddle
from CONSTANTS import *

if __name__ == '__main__':
    # Create screen
    screen = create_screen()

    # Create paddles
    paddle1 = Paddle(side=LEFT)
    paddle2 = Paddle(side=RIGHT)

    while True:
        screen.update()

    # screen.exitonclick()