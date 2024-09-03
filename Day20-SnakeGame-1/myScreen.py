from turtle import Screen
from CONSTANTS import SCREEN_SIZE


def create_screen():
    screen = Screen()
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.bgcolor('black')
    screen.title('My Snake Game')
    screen.tracer(0)  # turn animation off
    return screen
