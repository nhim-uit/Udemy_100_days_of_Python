from turtle import Turtle
from CONSTANTS import *
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.shapesize(1, 1, 1)
        self.setposition(0, 0)
        self.setheading(randint(30, 60))

    def move(self):
        if self.xcor() > WALL_WIDTH \
                or self.xcor() < -WALL_WIDTH:
            self.setheading(randint(75, 135) + self.heading())
        if self.ycor() > WALL_HEIGHT \
                or self.ycor() < -WALL_HEIGHT:
            self.setheading(randint(135, 180) + self.heading())

        self.forward(10)
