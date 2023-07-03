from math import pi
from decimal import Decimal


def isitradius(x):
    try:
        x = Decimal(x) > 0
        if x:   # if-else -> return x
            print("Alright")
            return True
        else:
            print("Radius cant be negative or 0")
            return False
    except:
        print("Invalid input")
        return False
 
   
r = input("Put your radius value: ")

while not isitradius(r):
    r = input("Please try again: ")   
 
f = Decimal(r)**2 * Decimal(str(pi))
print(f"Area of square with radius {r} is {round(f,2)}")