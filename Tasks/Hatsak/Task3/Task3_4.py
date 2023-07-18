"""4. Write a program that takes a list of numbers as input and returns the second largest number in the list."""
nums = [12, 2, 3, 4, 5, 6, 7, 8, 9]

nums.remove(max(nums))
print(max(nums))