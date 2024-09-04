from turtle import Turtle
import random


class MyTurtle(Turtle):
    def __init__(self, y, color, x=-230):
        super().__init__()
        self.color(color)
        self.penup()
        self.setposition(x, y)

    def move(self):
        self.forward(random.randint(0, 11))
