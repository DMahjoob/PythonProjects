# ITP 116, Spring 2024
# Lab 5
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825

import random

# Print initial options
print("Sentence Creator"
      "\n\tA) Add words"
      "\n\tB) Behold lists"
      "\n\tC) Create a sentence"
      "\n\tQ) Quit")

# Initialize the lists with starter values
nouns = ["sloth"]
verbs = ["frolicked"]
adverbs = ["joyfully"]

# Start the loop for user input, force choice to be uppercase
choice = (input("Enter a letter (A-C, Q): ")).upper()
while choice != "Q":
    if choice == "A":
        response = " "
        # Only add Nouns, Verbs, and Adverbs to appropriate lists
        # if their string length is greater than 0
        while len(response) > 0:
            response = input("Enter a noun (return to quit): ")
            nouns.append(response.strip())
        # Reset the response each time
        response = " "
        while len(response) > 0:
            response = input("Enter a verb (return to quit): ")
            verbs.append(response.strip())
        response = " "
        while len(response) > 0:
            response = input("Enter an adverb (return to quit): ")
            adverbs.append(response.strip())
        # Remove the last value from each list since it contains nothing
        nouns = nouns[:len(nouns)-1]
        verbs = verbs[:len(verbs) - 1]
        adverbs = adverbs[:len(adverbs)-1]
    elif choice == "B":
        print("nouns = " + str(nouns[:]))
        print("verbs = " + str(verbs[:]))
        print("adverbs = " + str(adverbs[:]))
    elif choice == "C":
        # Find random values in the size of the lists and print them out
        # while capitalizing the first letter
        randomNoun = random.randint(0, len(nouns)-1)
        randomVerb = random.randint(0, len(verbs)-1)
        randomAdverb = random.randint(0, len(adverbs)-1)
        print(str.capitalize(str.lower(nouns[randomNoun] + " " + verbs[randomVerb] + " " + adverbs[randomVerb] + ".")))
    else:
        print("Invalid choice")
    # Reset user choice
    choice = (input("Enter a letter (A-C, Q): ")).upper()