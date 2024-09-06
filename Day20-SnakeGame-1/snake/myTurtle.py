from turtle import Turtle
from CONSTANTS import PIXEL_SIZE


class MyTurtle(Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.shape('square')
        self.color('white')
        self.penup()
        self.setposition(x, y)
        self.shapesize(PIXEL_SIZE, PIXEL_SIZE, 1)
