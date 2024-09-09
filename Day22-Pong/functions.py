from turtle import Screen
from CONSTANTS import WIDTH, HEIGHT


def create_screen():
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title('Pong - Arcade Game')
    screen.bgcolor('black')
    screen.tracer(0)  # turn off animation
    return screen
