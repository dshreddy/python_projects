# Author : Sai Hemanth Reddy
# Date : 7 April 2023

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

##################################### Screen Settings #####################################################
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("Black")
screen.tracer(0)

##################################### Objects #####################################################
l_paddle = Paddle(1)
r_paddle = Paddle(2)
ball = Ball()
score_board = ScoreBoard()

##################################### Controls #####################################################
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


##################################### Game Play part #####################################################
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if abs(score_board.l_score-score_board.r_score) >= 3:
        ball.clear()
        score_board.game_over()
        game_is_on = False

    # Detect Collision of the ball with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision of the ball with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right Paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_score += 1
        score_board.update()

    # Left Paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_score += 1
        score_board.update()

screen.exitonclick()
