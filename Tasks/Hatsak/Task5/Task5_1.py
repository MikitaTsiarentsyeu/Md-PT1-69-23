"""1. Write a function that takes two integers as arguments and returns their sum."""


def summation(x='x', y='y'):
    print('This program will sum two numbers')
    if type(x+y) in (int, float):
        return x+y
    while not x.isdigit():
        x = input('Enter an integer: ')
    while not y.isdigit():
        y = input('Enter another integer: ')
    return int(x) + int(y)


print(summation(2, 3))