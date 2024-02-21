# ITP 116, Spring 2024
# Assignment 3
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825
# Description:
# This program determines whether a user has enough money
# to purchase various items

# Detect the user input and store their choice
print("Select a food item:")
print("a) Beaver Tail Pastry for $7.50")
print("b) Butter Tart for $3.00")
print("c) Nanaimo Bar for $4.85")
print("d) Poutine for $8.40")
choice = input("Choice: ")

# Use conditionals to determine order and cost
if(choice == 'a' or choice == 'A'):
    order = "Beaver Tail Pastry"
    cost = 750
elif(choice == 'b' or choice == 'B'):
    order = "Butter Tart"
    cost = 300
elif(choice == 'c' or choice == 'C'):
    order = "Nanaimo Bar"
    cost = 485
elif(choice == 'd'):
    order = "Poutine"
    cost = 840
else:
    print("\nYou entered an invalid choice.")
    print("The item selected is Beaver Tail Pastry.")
    order = "Beaver Tail Pastry"
    cost = 750

# Payment
print("\nPayment time!")
toonies = int(input("# of toonies you have: "))
loonies = int(input("# of loonies you have: "))
quarters = int(input("# of quarters you have: "))
nickels = int(input("# of nickels you have: "))

# Calculate and print user's money compared to cost
money = toonies*200 + loonies * 100 + quarters * 25 + nickels * 5

print("\nCost is " + str(cost) + " cents")
print("You have " + str(money) + " cents")

# Check if order worked
change = money-cost
if(change < 0):
    print("\nYou did not pay enough money and will not receive a " + order)
else:
    print("\nYou purchased the " + order)
    print("Your change is " + str(change) + " cents")
    # Returning Change in coins
    print("\nCoins Returned")
    print("# of toonies returned is " + str(change // 200))
    change %= 200
    print("# of loonies returned is " + str(change // 100))
    change %= 100
    print("# of quarters returned is " + str(change // 25))
    change %= 25
    print("# of nickels returned is " + str(change // 5))









