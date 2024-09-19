from turtle import Turtle
from CONSTANTS import *


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, -SIZE // 2 + PIXEL)
        self.color('black')
        self.shape('turtle')
        self.setheading(NORTH)

    def move(self):
        pass
