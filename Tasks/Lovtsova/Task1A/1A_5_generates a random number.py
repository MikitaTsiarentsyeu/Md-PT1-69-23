#5.Write a program that generates a random number between in a given range, and shows the answer to a user

import random

lower=input("to generate a random number, please enter the lower bound\n")
upper=input("to generate a random number, please enter the upper bound\n")
try:
    lower,upper=int(lower),int(upper)
    if lower>upper:
        lower,upper=upper,lower
    number=(random.randint(lower, upper))
    print(number)
except ValueError:
    print("Incorrect data entered! Please, enter the numbers again!\n")