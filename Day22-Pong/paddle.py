from MyTurtle import MyTurtle
from CONSTANTS import *


class Paddle:
    def __init__(self, side):
        self.__paddle = []
        self.create(side)

    def create(self, start_x=0, size=PIXEL):
        for i in range(size, -(size * 2), -size):
            t = MyTurtle(start_x, i)
            self.__paddle.append(t)
