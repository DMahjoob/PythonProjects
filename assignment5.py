# ITP 116, Spring 2024
# Assignment 5
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825
# Description:
# This program lets a user bet on their lucky numbers to win
# lots of points based on rolls from a 100-sided die
import random

win = False
count = 0
points = 0
num = "0"
winningNumbers = ""
while count < 5:
    while num != "1" and num != "2" and num != "3" and num != "4" and num != "5":
        num = input("Enter a number (1-5): ")
    print("You are playing for Case " + num)
    print("Winning numbers are ", end = " ")
    roll = random.randint(1, 101)
    if num == "1":
        for x in range(2, 101, 2):
            winningNumbers += str(x) + ", "
            if x == roll:
                win = True
    elif num == "2":
        for x in range(1, 100, 2):
            winningNumbers += str(x) + ", "
            if x == roll:
                win = True
    elif num == "3":
        for x in range(45, 66):
            winningNumbers += str(x) + ", "
            if x == roll:
                win = True
    elif num == "4":
        for x in range(10, 101, 10):
            winningNumbers += str(x) + ", "
            if x == roll:
                win = True
    else:
        for x in range(3, 100, 3):
            winningNumbers += str(x) + ", "
            if x == roll:
                win = True
    print(winningNumbers[:len(winningNumbers)-2])
    print("\nYou rolled a " + str(roll))
    if win:
        print("You win 50 points!")
        points += 50
    else:
        print("You didn't win.")
    print()
    winningNumbers = ""
    win = False
    num = 0
    count += 1

print("\nYour total score is " + str(points) + " points.")

