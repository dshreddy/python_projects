from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.setx(-230)
        self.sety(260)
        self.level_update()

    def level_update(self):
        self.level += 1
        self.clear()
        self.write(f"Level :{self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 50, "normal"))

