# 8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list.


user_input = input("Enter a list of numbers separated by commas: ")
numbers = [int(num) for num in user_input.split(",")]
average = sum(numbers) / len(numbers)
print("Average value:", average)