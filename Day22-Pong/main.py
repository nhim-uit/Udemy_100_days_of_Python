# Udemy: Master Python by building 100 projects in 100 days
# Sep 14, 2024
# Day 22 - Pong
# Created by me
# Create paddles
# Add auto moving paddles
# Add a ball and bouncing
# Detect walls and bouncing on paddles
# Add ball's moving speed
# Add scoreboard, game-over screen
from functions import *
from paddle import Paddle
from ball import Ball
from CONSTANTS import *
from scoreboard import ScoreBoard
import time

if __name__ == '__main__':
    # Create screen
    screen = create_screen()

    # Create paddles
    paddle_l = Paddle(side=LEFT_SIDE, direction=UP)
    paddle_r = Paddle(side=RIGHT_SIDE, direction=DOWN)

    # Create a ball
    ball = Ball()

    # Create a scoreboard
    scoreboard = ScoreBoard()

    # Control
    screen.listen()
    screen.onkey(paddle_l.up, 'w')
    screen.onkey(paddle_l.down, 's')
    screen.onkey(paddle_r.up, 'Up')
    screen.onkey(paddle_r.down, 'Down')

    game_on = True

    # Game on
    while game_on:
        screen.update()
        time.sleep(ball.move_speed)

        # Paddles move
        paddle_l.auto_move()
        paddle_r.auto_move()

        # Detect collision with paddles
        ball.detect_paddle(paddle_l)
        ball.detect_paddle(paddle_r)

        # Detect wall
        ball.detect_wall(scoreboard)

        # move
        ball.move()

        # game over
        game_on = scoreboard.game_over()

    screen.exitonclick()
