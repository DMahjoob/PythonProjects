# ITP 116, Spring 2024
# Assignment 6
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825
# Description: This program will select random words for the user to unscramble
# through a word-guessing game!

import random

# Create word bank and hints
wordBank = ['traveler', 'computer', 'coffee', 'workbook']
hints = ['horse', 'beep boop', 'java', 'writing']

# GAME START
while len(wordBank) > 0: # while wordBank still has words
    # Initialize variables and set up random word and corresponding hint
    rand = random.randint(0, len(wordBank) - 1)
    word = wordBank[rand]
    hint = hints[rand]
    jumbledWord = ""
    guess = ""
    numGuesses = 0

    # Split up word into letters
    letters = list(word)
    # Iterate through the word until the length of the jumbled word = the actual word
    while len(jumbledWord) < len(word):
        index = random.randint(0, len(letters) - 1)
        jumbledWord += letters[index]
        # Remove the used letter to prevent duplicates
        letters.remove(letters[index])
    print("\n" + str(len(wordBank)) + " word(s) to guess in the guessing game.")
    print("\nA random word has been picked for you, and it has " + str(len(word)) + " letters.")

    # While the guess is incorrect
    while guess != word:
        # Get user guess and increment guess counter
        print("The jumbled version of the word is \'" + jumbledWord + "\'")
        guess = (input("\nEnter your guess: ")).strip().lower()
        numGuesses += 1
        # Check for hint if word was not guessed correctly
        if guess != word:
            print("Your guess is incorrect.")
            response = (input("Do you want a hint (y or n)?")).lower()
            while response != 'y' and response != 'n':
                response = (input("Do you want a hint (y or n)?")).lower()
            if response == 'y':
                print("The hint is \'" + hint + "\'")

    # Remove words from wordBank and hints after they are gussed correctly
    wordBank.remove(word)
    hints.remove(hint)
    print("Correct! The number of guesses was " + str(numGuesses))
# GAME END
print("You guessed all the words!")
