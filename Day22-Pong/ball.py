from random import randint
from turtle import Turtle

from CONSTANTS import *
from paddle import Paddle
from scoreboard import ScoreBoard


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.shapesize(1, 1, 1)
        self.setposition(0, 0)
        self.setheading(randint(30, 60))
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        # move
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # move forward
        self.goto(new_x, new_y)

    def detect_wall(self, scoreboard: ScoreBoard):
        # detect right boundary
        if self.xcor() > WALL_WIDTH:
            scoreboard.l_point()
            self.goto(0, 0)
            self.bounce_x()
            self.move_speed = 0.1

        # detect left boundary
        if self.xcor() < -WALL_WIDTH:
            scoreboard.r_point()
            self.goto(0, 0)
            self.bounce_x()
            self.move_speed = 0.1

        # detect top and bottom
        if self.ycor() > WALL_HEIGHT \
                or self.ycor() < -WALL_HEIGHT:
            self.bounce_y()

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1

    def detect_paddle(self, paddle: Paddle):
        if self.distance(paddle.get_head()) < 50 and self.xcor() > WALL_WIDTH - 2 * PIXEL \
                or self.distance(paddle.get_head()) < 50 and self.xcor() < - WALL_WIDTH + 2 * PIXEL:
            self.bounce_x()

