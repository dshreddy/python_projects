# Author : Sai Hemanth Reddy
# Date : 7 April 2023

from turtle import Turtle

POSITIONS = [(0, 0), (-350, 0), (350, 0)]
UP_RANGE = 240
DOWN_RANGE = -215
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.color("Blue")
        self.penup()
        self.speed("fastest")
        # Initially it will be a square of size 20*20 I want it
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(POSITIONS[player])

    def up(self):
        if self.ycor() < UP_RANGE:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > DOWN_RANGE:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
