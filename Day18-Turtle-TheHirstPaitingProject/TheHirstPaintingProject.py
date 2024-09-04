# Udemy: Master Python by building 100 projects in 100 days
# Aug 27, 2024
# Day 18 - The Hirst Painting Project
import random

import colorgram
import turtle as t

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# print(rgb_colors)
tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
t.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()