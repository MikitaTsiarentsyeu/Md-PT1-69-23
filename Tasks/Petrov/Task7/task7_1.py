from decimal import Decimal, InvalidOperation


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero"


while True:
    try:
        nums = [Decimal(i) for i in input("Input 2 numbers by space: ").split()]
        print("Processing of dividing elements")
        print(f"Result is: {divide(*nums)}")
        break
    except InvalidOperation:
        print("Invalid operation")
    except TypeError:
        print("You need only 2 numbers")
