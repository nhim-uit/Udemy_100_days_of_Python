from MyTurtle import MyTurtle
from CONSTANTS import *


class Paddle:
    def __init__(self, side, direction):
        self.__paddle = MyTurtle(side, 0)
        self.__paddle.setheading(direction)

    def get_paddle(self):
        return self.__paddle

    def move(self):
        # Move forward by 1 pixel
        self.__paddle.forward(MOVE_DISTANCE)

    def auto_move(self):
        if self.__paddle.ycor() > EDGE:
            self.__paddle.setheading(DOWN)
        if self.__paddle.ycor() < -EDGE + PIXEL:
            self.__paddle.setheading(UP)
        self.move()

    def up(self):
        if self.__paddle.ycor() <= EDGE:
            self.__paddle.setheading(UP)
            self.move()

    def down(self):
        if self.__paddle.ycor() >= -EDGE + PIXEL:
            self.__paddle.setheading(DOWN)
            self.move()


