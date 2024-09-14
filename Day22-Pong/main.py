# Udemy: Master Python by building 100 projects in 100 days
# Sep 14, 2024
# Day 22 - Pong
# Created by me
# Create paddles
# Add auto moving paddles
# Add a ball and bouncing
from functions import *
from paddle import Paddle
from ball import Ball
from CONSTANTS import *
import time

if __name__ == '__main__':
    # Create screen
    screen = create_screen()

    # Create paddles
    paddle1 = Paddle(side=LEFT_SIDE, direction=UP)
    paddle2 = Paddle(side=RIGHT_SIDE, direction=DOWN)

    # Create a ball
    ball = Ball()

    # Control
    screen.listen()
    screen.onkey(paddle1.up, 'w')
    screen.onkey(paddle1.down, 's')
    screen.onkey(paddle2.up, 'Up')
    screen.onkey(paddle2.down, 'Down')

    game_on = True

    # Game on
    while game_on:
        screen.update()
        time.sleep(0.1)
        ball.move()
        paddle1.auto_move()
        paddle2.auto_move()



    # screen.exitonclick()