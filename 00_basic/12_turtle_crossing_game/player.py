from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('black')
        self.setheading(90)
        self.penup()
        self.refresh()

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def refresh(self):
        self.sety(-280)

