# Author : Sai Hemanth Reddy
# Date : 7 April 2023

from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 200)
        self.write(f"{self.l_score} {self.r_score}", align="center", font=("Courier", 80, "normal"))

    def update(self):
        self.clear()
        self.write(f"{self.l_score} {self.r_score}", align="center", font=("Courier", 80, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("Red")
        if self.l_score>self.r_score :
            s = " left "
        else: s = " right "
        self.write(f"Game Over\n "+s+"Player Won", align="center", font=("Courier", 66, "normal"))
