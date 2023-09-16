# Author : Sai Hemanth Reddy
# Date : 06 April 2023

from turtle import Turtle


class Snake:
    # Attributes of snake are starting positions , size (number of segments) & the direction in which it's headed
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    RIGHT = 0
    UP = 90
    LEFT = 180
    DOWN = 270
    segments = []

    # Constructor function of the initial 3 segment snake
    def __init__(self):
        for position in self.STARTING_POSITIONS:
            self.add_seg(position)

    # Methods of snake (Things that the snake does) are moving forward, turning left & right
    def add_seg(self, position):
        new_seg = Turtle("square")
        new_seg.color("red")
        new_seg.speed("fastest")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def clear(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.__init__()

    def extend(self):
        self.add_seg(self.segments[-1].position())

    # Method to move snake forward
    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())

        self.segments[0].forward(self.MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != self.DOWN:
            self.segments[0].setheading(self.UP)

    def down(self):
        if self.segments[0].heading() != self.UP:
            self.segments[0].setheading(self.DOWN)

    def left(self):
        if self.segments[0].heading() != self.RIGHT:
            self.segments[0].setheading(self.LEFT)

    def right(self):
        if self.segments[0].heading() != self.LEFT:
            self.segments[0].setheading(self.RIGHT)
