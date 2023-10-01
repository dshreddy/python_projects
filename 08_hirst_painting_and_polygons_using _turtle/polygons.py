from turtle import Turtle, Screen
from random import choice

colors = ["red", "green", "blue", "yellow", "orange", "violet", "pink"]

oogway = Turtle()

for j in range(3, 10):
    oogway.color(choice(colors))
    sides = j
    for i in range(j):
        oogway.forward(100)
        oogway.right(360/sides)


sc = Screen()
sc.exitonclick()
