from MyTurtle import MyTurtle
from CONSTANTS import *


class Paddle:
    def __init__(self, side, direction):
        self.__paddle = []
        self.create(side)
        self.__head = self.__paddle[0]
        self.__head.setheading(direction)

    def create(self, start_x=0, size=PIXEL):
        for i in range(size, -(size * 2), -size):
            t = MyTurtle(start_x, i)
            self.__paddle.append(t)

    def get_head(self):
        return self.__head

    def move(self):
        self.set_head_pos()
        for i in range(len(self.__paddle) - 1, 0, -1):
            new_x = self.__paddle[i - 1].xcor()
            new_y = self.__paddle[i - 1].ycor()
            self.__paddle[i].setposition(new_x, new_y)
        self.__head.forward(MOVE_DISTANCE)

    def set_head_pos(self):
        if self.__head.ycor() < -EDGE:
            self.__head.setheading(UP)
        if self.__head.ycor() > EDGE:
            self.__head.setheading(DOWN)


