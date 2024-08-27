from turtle import Turtle, Screen


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()
    tim.reset()


if __name__ == '__main__':
    tim = Turtle()
    screen = Screen()
    screen.listen()
    screen.onkey(key='w', fun=forward)
    screen.onkey(key='s', fun=backward)
    screen.onkey(key='a', fun=counter_clockwise)
    screen.onkey(key='d', fun=clockwise)
    screen.onkey(key='c', fun=clear)
    screen.exitonclick()