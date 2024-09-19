from turtle import Turtle
from CONSTANTS import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-EDGE, EDGE - PIXEL)
        self.level = 1
        self.write(f'Level: {self.level}',
                   move=False,
                   align='left',
                   font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align='center', font=FONT)
