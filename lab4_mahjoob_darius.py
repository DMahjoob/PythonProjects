# ITP 116, Spring 2024
# Lab 4
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825
# Description: Creates a passphrase based on user input to replace
# some letters with numbers and symbols

# Initialize variables
phraseCount = 1
phrase = ""
desire = True

# Run while loop as long as user wants to input sentences
while desire:
    phrase = input("Enter a phrase " + str(phraseCount) + " (q or Q to exit): ")
    # Check for user desire
    if phrase != "q" and phrase != "Q":
        modifiedPhrase = ""
        changeCount = 0
        # Run through every character in user input to generate a new encrpyted string
        for letter in phrase:
            if letter == 'A':
                modifiedPhrase += '4'
            elif letter == 'E':
                modifiedPhrase += '3'
            elif letter == 'I' or letter == 'i':
                modifiedPhrase += '1'
            elif letter == 'S':
                modifiedPhrase += '$'
            elif letter == 'T':
                modifiedPhrase += '7'
            elif letter == '1':
                modifiedPhrase += '!'
            else:
                modifiedPhrase += letter
                changeCount -= 1
            # Increment changeCount in every case except when the phrase character cannot be encrpyted
            changeCount +=1
        print("Your modified phrase " + str(phraseCount) + " is " + modifiedPhrase)
        print("Changed " + str(changeCount) + " characters")
        phraseCount += 1
    # Exit the loop in this case
    else:
        desire = False
print("Thank you!")