from decimal import Decimal, InvalidOperation
from functools import reduce


def divide(num1, num2):
    return num1 / num2


while True:
    try:
        nums = [Decimal(i) for i in input("Input 2 numbers by space: ").split()]
        print(f"Dividing {reduce(lambda x, y: f'{x} by {y}', nums)} equals {divide(*nums)}")
        # equals to line below:
        # print(f"Dividing {' by '.join(str(i) for i in nums)} equals {divide(*nums)}")
        break
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except InvalidOperation:
        print("Invalid operation")
    except TypeError:
        print("You need only 2 numbers")
