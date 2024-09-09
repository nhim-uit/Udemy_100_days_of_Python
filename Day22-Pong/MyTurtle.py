from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setposition(x, y)
        self.turtlesize(1, 1, 1)
