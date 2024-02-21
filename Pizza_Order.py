# ITP 116, Spring 2024
# Assignment 2
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825
# Description:
# This program allows for a user to create a script to order pizzas
# and calculate the total cost for them.

# Store user input in the following variables
name = input("Enter user name: ")
p_pizza = int(input("Enter the number of \"Pepperoni Pizza\" you would like to order: "))
v_pizza = int(input("Enter the number of \"Veggie Pizza\" you would like to order: "))
cof = int(input("Enter the number of \"Coffee\" you would like to order: "))
tea = int(input("Enter the number of \"Tea\" you would like to order: "))
ice_cream = float(input("Enter the dollar amount you would like to spend on ice-cream: "))

# Print the menu items for the story
print("\nMenu\nPepperoni Pizza: $12\nVeggie Pizza: $11\nCoffee: $5\nTea: $4.7\nTax and Tips : 30% of the total cost.\n")

# Calculate the total cost and tax/tip using user input
total_cost = p_pizza*12+v_pizza*11+cof*5+tea*4.7+ice_cream
tax_and_tip = total_cost * 0.3

# Round the total to the appropriate amount in US Dollars
final_total = round(total_cost + tax_and_tip, 2)

# Print out results in script format
print("Hello my name is \"" + name + "\". I would like to order")
print(str(p_pizza) + " \"Pepperoni Pizza\", " + str(v_pizza) + " \"Veggie Pizza\", ", end = "")
print(str(cof) + " \"Coffee\", and " + str(tea) + " \"Tea\".")
print("Also, can you give me $\'" + str(ice_cream) + "\' worth of ice-cream?")
print("I believe my total cost is $" + str(total_cost) + ".")
print("After the tax and tips, can you charge my card $" + str(final_total) + "? Thank you!")

