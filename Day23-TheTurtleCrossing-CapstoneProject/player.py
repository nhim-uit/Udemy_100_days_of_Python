from turtle import Turtle
from CONSTANTS import *


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
        if self.ycor() > SIZE // 2 - PIXEL:
            self.start_pos()

        self.forward(MOVE_DISTANCE)

    def start_pos(self):
        self.setposition(0, -SIZE // 2 + PIXEL)
