# Author : Sai Hemanth Reddy
# Date : 06 April 2023

from turtle import Turtle
from random import randint

RANGE = 270


class Food(Turtle):

    def __init__(self):
        # Since Food inherited from Turtle , food has color,shape,size,.... every thing that a Turtle has
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")

        self.goto(randint(-RANGE, RANGE), randint(-RANGE, RANGE))

    # Food has only one action, getting replaced when got eaten by snake

    def relocate(self):
        self.goto(randint(-RANGE, RANGE), randint(-RANGE, RANGE))
