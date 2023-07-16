"""Write a program that generates a random number in a given range,
and shows the answer to a user, ask a user for the left and right border"""

import random

print("Welcome! Here you can pick a random number from your range.")

left = input("Please, enter one border of your range:\n")
right = input("Please, enter another border of your range:\n")

if not left.isdigit() or not right.isdigit():
    print("Your input is incorrect. Please, enter an integer numeric value.")
    exit()

left, right = int(left), int(right)

if left > right:
    left, right = right, left

random_number = random.randint(left, right)
print("Your number is", random_number)
