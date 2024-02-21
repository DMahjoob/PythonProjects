# ITP 116, Spring 2024
# Lab 3
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825

import random
desire = True
count = 0

# Set the random number between 0-50 inclusive
number = random.randint(0, 50)
print("Computer: I selected a number between 0 and 50 (inclusive).")
print("Guess the number! Enter -1 to quit!")

# While loop to run the game until the user quits or gets the answer correct
while desire:
    guess = int(input("Guess(enter only numbers): "))
    if guess == -1:
        desire = False
    else:
        if number > guess:
            print("Go higher!")
        elif number < guess:
            print("Go lower!")
        else:
            desire = False
        count += 1

# Check game end condition, win or loss
if guess == -1:
    print("You lost. The number I guessed was " + str(number))
else:
    print("Great! That is correct!")
    print("You guessed the number in " + str(count) + " tries")