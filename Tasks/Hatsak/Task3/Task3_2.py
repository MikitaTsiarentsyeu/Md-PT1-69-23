"""2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list."""
nums = [1, 3, 2, 3, 2, 5, 11, 5]

print(sum([num for num in nums if num % 2 == 0]))