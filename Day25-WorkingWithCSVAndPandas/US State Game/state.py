from turtle import Turtle


class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(f'{state}', font=('Courier', 12, 'normal'))
        self.color('black')
