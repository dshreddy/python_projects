# Author : D. Sai Hemanth Reddy
# Date : 13 March

import turtle
import random
import colorgram


turtle.colormode(255)


def painting_generator(radius):
    colors = colorgram.extract('hirst.jpeg', 100)

    x_gap = int(3 * radius)
    y_gap = int(3 * radius)

    tim = turtle.Turtle()
    tim.hideturtle()
    tim.speed("fastest")
    tim.penup()
    tim.setheading(225)
    tim.forward(8*x_gap)
    tim.setheading(0)

    for i in range(8):
        for _ in range(10):
            tim.pendown()
            tim.dot(radius, random.choice(colors).rgb)
            tim.penup()
            tim.forward(x_gap)
        tim.backward(x_gap)

        tim.sety(int(tim.pos()[1]) + y_gap)
        tim.right(180)


painting_generator(15)

# For the screen to not go away after the execution of code
sc = turtle.Screen()
sc.exitonclick()
