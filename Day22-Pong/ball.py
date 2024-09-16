from turtle import Turtle
from CONSTANTS import *
from random import randint
from paddle import Paddle


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

    def move(self):
        # move
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # move forward
        self.goto(new_x, new_y)

    def detect_wall(self):
        """
        Detect collision with wall
        :return: False if collides with right or left wall
        """
        if self.xcor() > WALL_WIDTH \
                or self.xcor() < -WALL_WIDTH:
            self.goto(0, 0)
            self.bounce_x()
        if self.ycor() > WALL_HEIGHT \
                or self.ycor() < -WALL_HEIGHT:
            self.bounce_y()

        return True

    def bounce_x(self):
        # self.setheading(randint(75, 135) + self.heading())
        self.x_move *= -1

    def bounce_y(self):
        # self.setheading(randint(135, 180) + self.heading())
        self.y_move *= -1

    def detect_paddle(self, paddle: Paddle):
        if self.distance(paddle.get_head()) < 50 and self.xcor() > WALL_WIDTH - PIXEL \
                or self.distance(paddle.get_head()) < 50 and self.xcor() < - WALL_WIDTH + PIXEL:
            self.bounce_x()

