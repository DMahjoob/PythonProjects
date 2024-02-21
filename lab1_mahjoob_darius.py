# ITP 116, Spring 2024
# Lab 1
# Name: Darius Mahjoob
# Email: dmahjoob@usc.edu
# Section: 31825
# Description:63
# This program determines how many minutes, hours, and days
# are in a given user integer input

input = int(input("Enter the number of minutes: "))

day_to_min = 60 * 24
num_days = input // day_to_min
remainder = input % day_to_min
num_hours = remainder // 60
num_minutes = remainder % 60
print(str(input) + " minutes = " + str(num_days) + " days, " + str(num_hours) + " hours, and " + str(num_minutes) + " minutes")

