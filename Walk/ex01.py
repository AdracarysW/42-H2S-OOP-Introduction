#!/usr/bin/env python

# My program is a guessing game
# By awaraich


#The secret word: cinco

def guessing_game():
    print ("The secret word beings with a lower case 'c' ")
    for i in range(10):
        guess = input("GUESS: ")
        if (int(i)) == 9:
            print("Game Over")
        elif len(guess) == 0:
            print ("You have wasted a guess =P")
        elif len(guess) < 5 or len(guess) > 5:
            print ("0,1,2,3,4 that's how we count to five!")
        elif (guess[0] != "c"):
            print ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif guess == "cinco" and guess[0] == 'c':
            print ("Good Job! You are one with the Source.")
            break
        elif guess[0] == 'c':
            print ("You have " + str(9 - i) + " guesses left!")

def main():
    guessing_game()

main()
