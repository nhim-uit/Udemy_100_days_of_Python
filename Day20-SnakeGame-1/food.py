from turtle import Turtle
from random import randint
from CONSTANTS import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.set_random_position()

    def set_random_position(self):
        random_x = randint(-NO_OF_PIXEL, NO_OF_PIXEL) * PIXEL
        random_y = randint(-NO_OF_PIXEL, NO_OF_PIXEL) * PIXEL
        self.setposition(random_x, random_y)
