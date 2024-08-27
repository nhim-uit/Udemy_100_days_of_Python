import turtle as t
import random as r

tim = t.Turtle()

num_sides = 5

colours = ['red', 'blue', 'yellow', 'green', 'black', 'pink', 'orange']


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(r.choice(colours))
    draw_shape(shape_side_n)