# ITP 116, Spring 2024
# Assignment 4
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825
# Description:
# This program translates user-inputted words
# into a secret Elven language!

# Assign variables
choice = True
choice2 = True
sentence = ""
print("Welcome to the Elvish translator!")
# Initiate first loop for each translation
while choice:
    word = input("\nTranslate the following word: ")
    # Use index slicing to put the first letter at the end and lowercase all letters
    temp = (word[1:] + word[0]).lower()

    # Replace all k's with c's
    elvishWord = temp.replace("k", "c")

    # Check word length and apply suffix as according
    if len(word) < 4:
        elvishWord += "en"
    else:
        elvishWord += "i"
    print("\'" + word + "\' in elvish is " + elvishWord + "\n")

    # Build sentence
    sentence += " " + elvishWord

    #
    print("Enter A to enter another word.")
    print("Enter Q to build the sentence and then quit")
    choice2 = True
    while choice2:
        playAgain = input("Choice: ")
        if playAgain == 'a' or playAgain == 'A':
            choice2 = False
        elif playAgain == 'q' or playAgain == 'Q':
            choice = False
            choice2 = False
        else:
            print("You entered an invalid choice.")

sentence = sentence[1:]
sentence = sentence[0].upper() + sentence[1:]
print("\nYou have built the sentence: " + sentence + "\nOodbyegi")