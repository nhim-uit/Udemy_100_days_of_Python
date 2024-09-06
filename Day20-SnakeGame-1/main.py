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

from functions import *
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

game_on = True

# Move
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    detect_food(snake, food, scoreboard)

    # Detect collision with wall
    game_on = detect_wall(snake, scoreboard)
    if not game_on:
        break

    # Detect collision with tail
    game_on = detect_tail(snake, scoreboard)
    if not game_on:
        break

# exit on click
screen.exitonclick()
