# 4. Write a program that takes a list of numbers as input and returns the second largest number in the list.

user_input = input("Enter a comma-separated list of numbers: ")
num_list = [int(num) for num in user_input.split(",")]
num_list.sort(reverse=True)
print("Second largest number on the list:", num_list[1])