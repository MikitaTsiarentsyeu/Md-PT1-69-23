# 5. Write a program that generates a random number in a given range,
# and shows the answer to a user, ask a user for the left and right border.

import random

while True:
    try:
        a = int(input("Enter the first number:\n "))
        b = int(input("Enter the second number:\n "))
        if a >= b:
            print("The second number must be greater than the first")
            continue
        print("Random number: ", random.randrange(a, b))
    except ValueError:
        print("Error! Enter whole numbers")
    break