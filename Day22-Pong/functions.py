from turtle import Screen
from paddle import Paddle
from ball import Ball
from CONSTANTS import *
from scoreboard import ScoreBoard
import time


def create_screen():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title('Pong - Arcade Game')
    screen.bgcolor('black')
    screen.tracer(0)  # turn off animation
    return screen


def run():
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
