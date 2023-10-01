import random
import hangman_words
import hangman_ascii

# Intro prompt
def intro():
    print("Welcome to Hangman !")
    print("\nRules of the game :")
    print("1) There is an unkown word for you to find out")
    print("2) You have to guess the letters in it")
    print("3) For each wrong guess a part of man's body is hanged to death")

intro()

# Game function
def game():

    # Choosing a word for game
    random_word = random.choice(hangman_words.word_list)
    n = len(random_word)

    # Creating a list with n blanks "_ _ _ ... _ _"
    guess = []
    for i in range(n):
        guess.append('_ ')

    # body indicates the number of parts hanging
    body = 0

    # Play game while body <= 10
    while 1:

        # Taking user guess character
        ch = input("\nEnter a letter\n")

        # Checking if entered character is there in the actual word
        flag = 0
        for i in range(n):
            if random_word[i] == ch:
                guess[i] = ch
                flag = 1

        # Updating the guessed answer
        ans = ''
        for i in range(n):
            print(guess[i], end=' ')
            ans += guess[i]

        # Wrong guess
        if flag == 0:
            body += 1
            hangman_ascii.hang(body)
            print("Lives left : "+str(7-body))
            if body == 7:
                print("\nYou Lost The word is "+random_word+" \n")
                break

        # Winning case
        if ans == random_word:
            print("\nYou Won\n")
            break

game()
