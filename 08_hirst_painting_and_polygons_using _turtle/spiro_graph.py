import random
import turtle
from turtle import Turtle, Screen


turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim = Turtle()
tim.speed("fastest")


def spirograph(gap):
    n = int(360/gap)
    for i in range(n):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


spirograph(10)
sc = Screen()
sc.exitonclick()
