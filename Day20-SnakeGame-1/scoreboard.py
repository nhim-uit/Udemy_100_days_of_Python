from turtle import Turtle
from CONSTANTS import ALIGNMENT, FONT, TOP_X, TOP_Y


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.get_high_score()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(TOP_X, TOP_Y)
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score} - High Score: {self.high_score}',
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER',
                   move=False,
                   align=ALIGNMENT,
                   font=FONT)

    def reset(self):
        self.get_high_score()

        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()

        self.score = 0
        self.update()

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def write_file(self):
        with open('score.txt', 'w') as file:
            file.write(f'{self.high_score}')

    def get_high_score(self):
        try:
            with open('score.txt', 'r') as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
            self.write_file()
