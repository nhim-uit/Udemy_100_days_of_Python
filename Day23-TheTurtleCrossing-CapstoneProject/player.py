from turtle import Turtle
from CONSTANTS import *
from scoreboard import Scoreboard


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setheading(NORTH)
        self.start_pos()

    def move(self):
        # detect_top
        if self.ycor() > EDGE:
            self.start_pos()

        self.forward(MOVE_DISTANCE)

    def start_pos(self):
        self.goto(0, -SIZE // 2)
