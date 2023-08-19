"""task 7-1. Write a function that takes two numbers as input and returns their division.
Handle the ZeroDivisionError and return "Cannot divide by zero" if the denominator is zero."""


def division_function():
        numerator = input("Please, enter the numerator:\n")
        denominator = input("Please, enter the denominator:\n")
        try:
            return print(f'The answer is {float(numerator) / float(denominator)}')

        except ValueError:
            print("Please, enter only numbers")

        except ZeroDivisionError:
            print('Cannot divide by zero')


division_function()
