import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


###################################### Screen settings ###############################################
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.listen()
screen.tracer(0)

###################################### Objects ###############################################
turtle = Player()
score_board = Scoreboard()
car_manager = CarManager()

###################################### CONTROLS ###############################################
screen.onkey(fun=turtle.up, key="Up")

###################################### Game play ###############################################
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars
    car_manager.create_car()
    car_manager.move_cars()

    # If reaches other end restart the game
    if turtle.ycor() == 250:
        turtle.refresh()
        car_manager.speed_up()
        score_board.level_update()

    # If hits a car edge then it's game over
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            score_board.game_over()
            screen.update()
            game_is_on = False

screen.exitonclick()
