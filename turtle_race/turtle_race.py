# Author : D. Sai Hemanth Reddy
# Date : 13 March 2023

# Import necessary modules
import random
from turtle import Turtle, Screen

# Initialize the screen
sc = Screen()
sc.setup(width=800, height=600)


# Define the main game function
def game():
    # Define a list of colors for the turtles to choose from
    colors = ["red", "blue", "green", "yellow", "orange", "pink", "violet", "black", "brown"]

    # Create a list of five turtles and set their properties
    t = [0 for i in range(5)]
    for i in range(5):
        t[i] = Turtle(shape="turtle")
        t[i].speed("fastest")
        t[i].penup()
        t[i].color(random.choice(colors))

    # Set the starting positions of the turtles
    t[4].goto(-380, -200)
    t[3].goto(-380, -100)
    t[1].goto(-380, 100)
    t[0].goto(-380, 200)
    t[2].goto(-380, 0)

    # Define a list of allowed values for the user's bet
    allowed_values = ['0', '1', '2', '3', '4']

    # Prompt the user to enter a bet until they enter a valid number
    user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race ? (Enter a number [0,4])")
    while user_bet not in allowed_values:
        user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race ? (Enter a number [0,4])")

    # Define the function to move the turtles forward at each iteration
    def race():
        t[0].forward(random.randint(0, 10))
        t[1].forward(random.randint(0, 10))
        t[2].forward(random.randint(0, 10))
        t[3].forward(random.randint(0, 10))
        t[4].forward(random.randint(0, 10))

    # Run the race until one of the turtles reaches a certain point on the screen
    while t[0].pos()[0] < 360 and t[1].pos()[0] < 360 and t[2].pos()[0] < 360 and t[3].pos()[0] < 360 and t[4].pos()[
        0] < 360:
        race()

    # Create a list of tuples containing the turtles' final positions and their index numbers
    res = []
    res.append((t[0].pos()[0], 0))
    res.append((t[1].pos()[0], 1))
    res.append((t[2].pos()[0], 2))
    res.append((t[3].pos()[0], 3))
    res.append((t[4].pos()[0], 4))

    # Sort the list of tuples in descending order based on the turtles' final positions
    res.sort()
    res.reverse()

    # Determine the winner(s) of the race
    if res[0][0] != res[1][0]:
        pr = '''Press 1 to play again, any other key to exit
        ''' + "Winner(s) =" + str(res[0][1])
    else:
        pr = '''Press 1 to play again, any other key to exit
        ''' + "Winner(s) =" + str(res[0][1])
        i = 1
        while i <= 4 and res[i][0] == res[0][0]:
            pr += " " + str(res[i][1])
            i += 1

    # Print the game result on the screen and ask if the user wants to play again
    if t[int(user_bet)].pos()[0] >= 360:

        inp = sc.textinput(title="You Won", prompt=pr)
        if inp == '1':
            sc.clear()
            game()
    else:
        inp = sc.textinput(title="You Lost", prompt=pr)
        if inp == '1':
            sc.clear()
            game()


# First game call
game()
