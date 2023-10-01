#A project useful to understand random module

import random

#Choosing
user_choice=int(input("What do you choose ? [Type 0 for Rock, 1 for Paper & 2 for scissors]\n"))
system_choice = random.randint(0,2)

#Printing what each chose
rock='''
_ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''
paper='''
_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| 
'''
scissors='''                  
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \___
|___/\___|_|___/___/\___/|_|  |___/
'''

if (user_choice==0) : print(rock)
elif (user_choice==1) : print(paper)
else : print(scissors)


if (system_choice==0) : print(rock)
elif (system_choice==1) : print(paper)
else : print(scissors)

#Game Result
if (user_choice==0 and system_choice==2) or (user_choice==1 and system_choice==0) or (user_choice==2 and system_choice==1): 
    print("You Won :)")
elif user_choice==system_choice :
    print("Draw")
else :
    print("You Lost :(")
