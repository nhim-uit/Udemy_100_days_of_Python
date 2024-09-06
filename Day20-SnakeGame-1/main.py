# Udemy: Master Python by building 100 projects in 100 days
# Aug 28 - Sep 6, 2024
# Day 20 - Snake Game
# Created based on Udemy course
# Modified by me
# Version 1
# OOP - encapsulation, inheritance
# no docstrings, no try catch
# ---------------------------------------------------------
# Create a snake body
# Move the snake
# Control the snake
# Detect collision with food
# Scoreboard, game-over
# Detect collision with wall
# Detect collision with tail

from snake.mySnake import Snake
from myScreen import *
from food import Food
from scoreboard import ScoreBoard
from CONSTANTS import EDGE
import time

# Create Screen
screen = create_screen()

# Create snake body (3 turtles)
snake = Snake()

# Create food
food = Food()

# Create score board
scoreboard = ScoreBoard()

# Snake's controls
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True

# Move
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.get_head().distance(food) <= 10:
        snake.extend()
        food.set_random_position()
        scoreboard.increase()

    # Detect collision with wall
    if snake.get_head().xcor() > EDGE \
            or snake.get_head().xcor() < -EDGE \
            or snake.get_head().ycor() > EDGE \
            or snake.get_head().ycor() < -EDGE:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for s in (snake.get_snake())[1:]:
        if snake.get_head().distance(s) <= 10:
            game_on = False
            scoreboard.game_over()

# exit on click
screen.exitonclick()
