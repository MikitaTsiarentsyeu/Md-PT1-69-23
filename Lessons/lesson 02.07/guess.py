import random

my_number = random.randint(1, 10)
# print(my_number)

your_number = input("Guess my number (from 1 to 10):\n")

if not your_number.isdigit():
    print("Your input was not an integer number")
    exit()

your_number = int(your_number)

if your_number < 1 or your_number > 10:
    print("Your number was not in correct range")
    exit()

if my_number == your_number:
    print("Lucky guess!")
else:
    print("Looooser!")