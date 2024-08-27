from turtle import Turtle
import random


class MyTurtle:
    def __init__(self, y, color, x=-230):
        self.__t = Turtle('turtle')
        self.__t.color(color)
        self.__t.penup()
        self.__t.setposition(x, y)

    def get_turtle(self) -> Turtle:
        return self.__t

    def move(self):
        self.__t.forward(random.randint(0, 11))
