from turtle import Screen
from CONSTANTS import SCREEN_SIZE, EDGE
from food import Food
from snake.mySnake import Snake
from scoreboard import ScoreBoard


def create_screen():
    screen = Screen()
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.bgcolor('black')
    screen.title('My Snake Game')
    screen.tracer(0)  # turn animation off
    return screen


def detect_food(snake: Snake, food: Food, scoreboard: ScoreBoard):
    if snake.get_head().distance(food) <= 10:
        snake.extend()
        food.set_random_position()
        scoreboard.increase()


def detect_wall(snake: Snake, scoreboard: ScoreBoard):
    if snake.get_head().xcor() > EDGE \
            or snake.get_head().xcor() < -EDGE \
            or snake.get_head().ycor() > EDGE \
            or snake.get_head().ycor() < -EDGE:
        scoreboard.game_over()
        return False
    return True


def detect_tail(snake: Snake, scoreboard: ScoreBoard):
    for s in (snake.get_snake())[1:]:
        if snake.get_head().distance(s) <= 10:
            scoreboard.game_over()
            return False
    return True
