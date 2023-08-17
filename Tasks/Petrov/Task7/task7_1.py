from decimal import Decimal, InvalidOperation


def divide(num1: Decimal, num2: Decimal) -> Decimal:
    """Return the result of division of two numbers"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero"


while True:
    try:
        print("Input 2 numbers by space:", end=" ")

        # Creating list of numbers to calculate their division
        nums = [Decimal(i) for i in input().split()]

        print("Processing of dividing elements")
        print(f"Result is: {divide(*nums)}")
        break
    except InvalidOperation:

        # If input can't be converted to Decimal, InvalidOperation raises
        # It also raises for [0, 0] and [inf, inf] cases
        print("Invalid operation")

    except TypeError:

        # If the list has more than 2 numbers, TypeError raises
        print("You need only 2 numbers")
