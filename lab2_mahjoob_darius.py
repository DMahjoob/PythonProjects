# ITP 116, Spring 2024
# Lab 2
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825

# Determine user 1's Zodiac Sign
year1 = int(input("Enter year for user 1: "))
val1 = year1 % 12
if(val1 == 0):
    print(str(year1) + " is the Year of the Monkey.")
elif(val1== 1):
    print(str(year1) + " is the Year of the Rooster.")
elif(val1 == 2):
    print(str(year1) + " is the Year of the Dog.")
elif(val1 == 3):
    print(str(year1) + " is the Year of the Pig.")
elif(val1 == 4):
    print(str(year1) + " is the Year of the Rat.")
elif(val1 == 5):
    print(str(year1) + " is the Year of the Ox.")
elif(val1 == 6):
    print(str(year1) + " is the Year of the Tiger.")
elif(val1 == 7):
    print(str(year1) + " is the Year of the Rabbit.")
elif(val1 == 8):
    print(str(year1) + " is the Year of the Dragon.")
elif(val1 == 9):
    print(str(year1) + " is the Year of the Snake.")
elif(val1 == 10):
    print(str(year1) + " is the Year of the Horse.")
else:
    print(str(year1) + " is the Year of the Goat.")

# Determine user 2's Zodiac Sign
year2 = int(input("enter year for user 2: "))
val2 = year2 % 12
if(val2 == 0):
    print(str(year2) + " is the Year of the Monkey.")
elif(val2 == 1):
    print(str(year2) + " is the Year of the Rooster.")
elif(val2 == 2):
    print(str(year2) + " is the Year of the Dog.")
elif(val2 == 3):
    print(str(year2) + " is the Year of the Pig.")
elif(val2 == 4):
    print(str(year2) + " is the Year of the Rat.")
elif(val2 == 5):
    print(str(year2) + " is the Year of the Ox.")
elif(val2 % 12 == 6):
    print(str(year2) + " is the Year of the Tiger.")
elif(val2 % 12 == 7):
    print(str(year2) + " is the Year of the Rabbit.")
elif(val2 % 12 == 8):
    print(str(year2) + " is the Year of the Dragon.")
elif(val2 % 12 == 9):
    print(str(year2) + " is the Year of the Snake.")
elif(val2 == 10):
    print(str(year2) + " is the Year of the Horse.")
else:
    print(str(year2) + " is the Year of the Goat.")

# Check if Zodiac signs are the same
if(val1 == val2):
    print("Both user share the same Zodiac animal!")


