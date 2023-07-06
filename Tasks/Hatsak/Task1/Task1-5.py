"""5.Write a program that generates a random number in a given range,
 and shows the answer to a user, ask a user for the left and right border."""
import random
print("This program will generate a random number from A to B.")


r = input("Enter A: ")
l = input("Enter B: ")

if (l+r).isdigit():
    print(random.randint(int(r), int(l)))
else:
    print("You should choose only integers!")
