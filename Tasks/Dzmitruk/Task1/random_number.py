# a program which generates a random number in a given range, and shows the answer to a user

import random

a = input("Enter a left border: ")

while not a.isdigit():
    print("The value is wrong.")
    a = input("Enter a left border: ")

b = input("Enter a right border: ")

while not b.isdigit():
    print("The value is wrong.")
    b = input("Enter a right border: ")

a = int(a)
b = int(b)

if a>b:
    print( f"Random number in a given range is {random.randrange(a,b,-1)}")

else:
    print(random.randint(a,b))

