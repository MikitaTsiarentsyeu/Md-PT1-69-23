"""2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list."""
from list_input import enter

nums = enter()
print(sum([num for num in nums if num % 2 == 0]))
