import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim = t.Turtle()
t.colormode(255)

# colours = ['red', 'blue', 'yellow', 'green', 'black', 'pink', 'orange', 'brown']
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')

for _ in range(500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))