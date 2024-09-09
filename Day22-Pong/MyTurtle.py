from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setposition(x, y)
        self.shapesize(stretch_wid=1, stretch_len=5)
