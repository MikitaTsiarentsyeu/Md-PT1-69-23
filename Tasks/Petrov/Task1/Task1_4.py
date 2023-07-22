from decimal import Decimal, InvalidOperation
from random import randint


def isitamount(x):
    try:
        x = Decimal(x) > 0
        if x:   # if-else -> return x
            print("Alright")
            return True
        else:
            print("Money cant be negative or 0")
            return False
    except InvalidOperation:
        print("Invalid input")
        return False


usd = input("Put how much money do you have: ")

while not isitamount(usd):
    usd = input("Please try again: ")

r1 = randint(2, 3)
r2 = randint(0, 100)
ratio = Decimal(f"{r1}.{r2}")
print(f"Today's ratio is 1 USD = {ratio} BYN")

byn = Decimal(usd) * ratio
print(f"with {usd} USD you have {byn} BYN")
