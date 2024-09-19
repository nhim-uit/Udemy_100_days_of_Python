import time
from turtle import Screen
from CONSTANTS import *
from player import Player
from cars import Cars


def create_screen():
    screen = Screen()
    screen.setup(width=SIZE, height=SIZE)
    screen.title('The Turtle Crossing Game')
    screen.bgcolor('white')
    screen.tracer(0)  # turn off animation
    return screen


def level_up(player: Player, cars: Cars):
    if player.ycor() > SIZE // 2:
        for car in cars.get_cars():
            car.speed_up()


def run():
    # Create Screen
    screen = create_screen()

    # Create player
    player = Player()

    # Create cars
    cars = Cars()

    game_on = True

    while game_on:
        time.sleep(0.1)
        screen.update()

        player.move()
        cars.move()
        level_up(player, cars)



    screen.exitonclick()
