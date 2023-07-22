# 1. Write a program that takes a string as input from a user and returns the number of vowels in the string.


user_input = input("Enter the string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in user_input:
    if char.lower() in vowels:
        count += 1
print("Number of vowels in a line:", count)