# Author : Sai Hemanth Reddy
# Date : 06 April 2023

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")

        with open("high_score.txt") as file:
            self.high_score = int(file.read())

        self.penup()
        self.goto(0, 280)
        self.score = -1
        self.hideturtle()

    # Score board has only one action getting updated whenever food is eaten

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score} High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("high_score.txt", mode='w') as file:
                file.write(str(self.high_score))

        self.score = -1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

