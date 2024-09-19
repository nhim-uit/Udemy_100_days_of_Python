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
        self.move_speed = STARTING_MOVE_SPEED

    def move(self):
        if self.xcor() < -SIZE // 2:
            self.setposition(SIZE // 2, randint(-EDGE, EDGE))

        self.forward(self.move_speed)

    def start_pos(self):
        self.setposition(randint(-EDGE, EDGE),
                         randint(-EDGE, EDGE))

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
