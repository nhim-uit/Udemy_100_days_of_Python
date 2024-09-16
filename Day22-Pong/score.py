from turtle import Turtle
from CONSTANTS import ALIGNMENT, FONT


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.update()

    def update(self):
        self.clear()
        self.write(f'{self.score}',
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def increase(self):
        self.score += 1

    def get_score(self):
        return self.score
