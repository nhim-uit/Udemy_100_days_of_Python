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


def level_up(player: Player, cars: Cars, scoreboard: Scoreboard):
    if player.ycor() > EDGE:
        for car in cars.get_cars():
            car.speed_up()
        scoreboard.increase()


def detect_collision(player: Player, cars: Cars):
    for car in cars.get_cars():
        if car.distance(player) < PIXEL:
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
        level_up(player, cars, scoreboard)

        game_on = detect_collision(player, cars)

        if not game_on:
            scoreboard.game_over()

    screen.exitonclick()
