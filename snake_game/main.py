# Author : Sai Hemanth Reddy
# Date : 06 April 2023

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Making a screen for our game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Creating our snake, food, sc˳ore board on the screen
snake = Snake()
food = Food()
score_board = ScoreBoard()
score_board.update()

# Controlling snake using keyboard
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Playing until the player hits wall or some segment of tail
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.relocate()
        score_board.update()
        snake.extend()

    # Detect Collision with the wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() < -290 or \
            snake.segments[0].ycor() > 290:
        snake.clear()
        score_board.reset()

    # Detect Collision with Tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            snake.clear()
            score_board.reset()

# without this the screen goes away after code execution, which leads us to not observe what happened in the end
screen.exitonclick()
