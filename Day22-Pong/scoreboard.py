from turtle import Turtle
from score import Score
from CONSTANTS import ALIGNMENT, FONT


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = Score(-100, 250)
        self.score2 = Score(100, 250)
        # self.score1.update()
        # self.score2.update()

    def l_point(self):
        self.score1.increase()
        self.score1.update()

    def r_point(self):
        self.score2.increase()
        self.score2.update()

    def game_over(self):
        if abs(self.score1.get_score() - self.score2.get_score()) == 1:
            self.score1.clear()
            self.score2.clear()

            self.goto(0, 0)
            self.color('white')
            self.hideturtle()
            self.penup()
            self.write('GAME OVER\n'
                       f'{self.score1.get_score()}: {self.score2.get_score()}',
                       move=False,
                       align=ALIGNMENT,
                       font=FONT)
            return False
        return True
