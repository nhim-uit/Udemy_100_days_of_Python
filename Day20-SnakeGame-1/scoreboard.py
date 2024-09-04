from turtle import Turtle
from CONSTANTS import ALIGHTMENT, FONT, TOP_X, TOP_Y


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(TOP_X, TOP_Y)
        self.update()

    def update(self):
        self.write(f'Score: {self.score}',
                   move=False,
                   align=ALIGHTMENT,
                   font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

