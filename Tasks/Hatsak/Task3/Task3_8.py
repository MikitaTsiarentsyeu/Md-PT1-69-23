"""8. Write a program that takes a list of numbers as
 input and returns the average of all numbers in the list."""
from list_input import enter

nums = enter()


def average(arr):
    return sum(arr)/len(arr)


print(average(nums))
