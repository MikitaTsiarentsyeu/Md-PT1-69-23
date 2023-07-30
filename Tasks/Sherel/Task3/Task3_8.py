"""8. Write a program that takes a list of numbers as input and returns the average of all numbers in the list."""

user_input = input("Enter your list of numbers separated by a space:\n")
user_input = user_input.split()

sum_num = 0
for num in user_input:
    sum_num += int(num)

print(sum_num/len(user_input))