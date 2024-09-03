from snake.myTurtle import MyTurtle
from CONSTANTS import *


class Snake:
    def __init__(self):
        self.__snake = []
        self.create()
        self.__head = self.__snake[0]

    def create(self, size=PIXEL):
        # set colors to differentiate 3 pixels
        colors = ['red', 'green', 'blue']
        j = 0
        for i in range(0, -(size * 2 + 1), -size):
            t = MyTurtle(x=i)
            t.color(colors[j])
            j += 1
            self.__snake.append(t)

    def get_head(self):
        return self.__head

    def move(self):
        for i in range(len(self.__snake) - 1, 0, -1):
            new_x = self.__snake[i - 1].xcor()
            new_y = self.__snake[i - 1].ycor()
            self.__snake[i].setposition(new_x, new_y)

        self.__head.forward(MOVE_DISTANCE)

    def up(self):
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)

    def right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)

    def left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)
