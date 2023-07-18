"""8. Write a program that takes a list of numbers as
 input and returns the average of all numbers in the list."""

nums = [1, 2, 3, 3]


def average(arr):
    return sum(arr)/len(arr)


print(average(nums))
