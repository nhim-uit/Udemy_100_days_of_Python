# Udemy: Master Python by building 100 projects in 100 days
# Aug 28 - Sep 3, 2024
# Day 20 - Snake Game
# Created based on Udemy course
# Modified by me
# Version 1
# OOP - encapsulation, inheritance
# no docstrings
# ---------------------------------------------------------
# Create a snake body
# Move the snake
# Control the snake
# Detect collision with food
# Scoreboard

from snake.mySnake import Snake
from myScreen import *
from food import Food
from scoreboard import ScoreBoard
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

# Move
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.get_head().distance(food) <= 10:
        food.set_random_position()
        scoreboard.increase()


# exit on click
screen.exitonclick()
