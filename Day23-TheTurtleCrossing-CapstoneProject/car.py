from turtle import Turtle
from random import randint, choice
from CONSTANTS import *


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(WEST)
        self.start_pos()
        self.move_speed = 5

    def move(self):
        if self.xcor() < -SIZE // 2:
            self.setposition(SIZE // 2 - PIXEL, randint(-SIZE // 2 + PIXEL, SIZE // 2 - PIXEL))

        self.forward(self.move_speed)

    def start_pos(self):
        self.setposition(randint(-SIZE // 2 + PIXEL, SIZE // 2 - PIXEL),
                         randint(-SIZE // 2 + PIXEL, SIZE // 2 - PIXEL))

    def speed_up(self):
        self.move_speed += 5
