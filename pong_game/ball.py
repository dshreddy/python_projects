# Author : Sai Hemanth Reddy
# Date : 7 April 2023

import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Blue")
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = -10

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()



