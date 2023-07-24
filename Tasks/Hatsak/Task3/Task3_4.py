"""4. Write a program that takes a list of numbers as input and returns the second largest number in the list."""
from list_input import enter

nums = enter()
nums.remove(max(nums))
print(max(nums))
