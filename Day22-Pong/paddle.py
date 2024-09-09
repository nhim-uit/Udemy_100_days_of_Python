from MyTurtle import MyTurtle
from CONSTANTS import *


class Paddle:
    def __init__(self, side, direction):
        self.__paddle = []
        self.create(side)
        self.__head = self.__paddle[0]
        self.__head.setheading(direction)

    def create(self, start_x=0, size=PIXEL):
        self.__paddle.append(MyTurtle(start_x, 0))

    def get_head(self):
        return self.__head

    def move(self):
        # Move forward by 1 pixel
        self.__head.forward(MOVE_DISTANCE)

    def auto_move(self):
        if self.__head.ycor() > EDGE:
            self.__head.setheading(DOWN)
        if self.__head.ycor() < -EDGE + PIXEL:
            self.__head.setheading(UP)
        self.move()

    def up(self):
        if self.__head.ycor() <= EDGE:
            self.__head.setheading(UP)
            self.move()

    def down(self):
        if self.__head.ycor() >= -EDGE + PIXEL:
            self.__head.setheading(DOWN)
            self.move()


