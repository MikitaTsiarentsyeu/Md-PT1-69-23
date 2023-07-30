#5.Write a program that generates a random number between in a given range, and shows the answer to a user

import random

lower=input("to generate a random number, please enter the lower bound\n")
upper=input("to generate a random number, please enter the upper bound\n")
lower,upper=int(lower),int(upper)
number=int(random.randint(lower, upper))

print(number)