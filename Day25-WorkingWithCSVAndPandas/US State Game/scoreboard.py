from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.__score = 0
        self.penup()
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.write(f'{self.__score}', font=('Courier', 12, 'normal'))

    def increase(self):
        self.__score += 1

    @property
    def score(self):
        return self.__score
