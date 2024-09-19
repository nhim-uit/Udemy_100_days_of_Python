import time
from turtle import Screen
from CONSTANTS import *
from player import Player
from cars import Cars
from scoreboard import Scoreboard


def create_screen():
    screen = Screen()
    screen.setup(width=SIZE, height=SIZE)
    screen.title('The Turtle Crossing Game')
    screen.bgcolor('white')
    screen.tracer(0)  # turn off animation
    return screen


def level_up(player: Player, cars: Cars):
    if player.ycor() > EDGE:
        for car in cars.get_cars():
            car.speed_up()


def detect_collide(player: Player, cars: Cars):
    for car in cars.get_cars():
        if player.distance(car) < PIXEL:
            return False
    return True


def run():
    # Create Screen
    screen = create_screen()

    # Create player
    player = Player()

    # key listen
    screen.listen()
    screen.onkey(player.move, 'Up')

    # Create cars
    cars = Cars()

    # Create scoreboard
    scoreboard = Scoreboard()

    game_on = True

    while game_on:
        time.sleep(0.1)
        screen.update()

        cars.move()
        level_up(player, cars)

        game_on = detect_collide(player, cars)

        if not game_on:
            scoreboard.game_over()

    screen.exitonclick()
