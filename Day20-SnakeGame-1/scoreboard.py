from turtle import Turtle
from CONSTANTS import ALIGNMENT, FONT, TOP_X, TOP_Y


# noinspection PyArgumentList
def retrieve_high_score():
    try:
        with open('score.txt', 'r') as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
        with open('score.txt', 'w') as file:
            file.write(f'{high_score}')

    return high_score


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.__score = 0
        self.__high_score = retrieve_high_score()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(TOP_X, TOP_Y)
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.__score} - High Score: {self.__high_score}',
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
        if self.__score > self.__high_score:
            self.__high_score = self.__score

            with open('score.txt', 'w') as file:
                file.write(f'{self.__high_score}')

        self.__score = 0
        self.update()

    def increase(self):
        self.__score += 1
        self.clear()
        self.update()

    @property
    def high_score(self):
        return self.__high_score

    @high_score.setter
    def high_score(self, h_score):
        self.__high_score = h_score

    @property
    def score(self):
        return self.__score
