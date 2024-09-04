from MyTurtle import *
from CONSTANTS import *
from functions import compare


class Turtles:
    def __init__(self):
        self.__turtles = []

    def create(self):
        y = -100
        for c in COLORS:
            t = MyTurtle(y, c)
            y += 30

            self.__turtles.append(t)

    def race(self, user_color):
        is_race_on = True

        while is_race_on:
            for t in self.__turtles:
                # stop when a turtle's x reach 230
                if t.xcor() > 230:
                    is_race_on = False
                    winning_color = t.pencolor()
                    compare(user_color, winning_color)

                t.move()
