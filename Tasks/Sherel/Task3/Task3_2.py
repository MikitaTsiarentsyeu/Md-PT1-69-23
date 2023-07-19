"""2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list."""

user_input = input("Enter your list of numbers separated by a space:\n")
user_input = user_input.split()

sum_num = 0
for num in user_input:
    if int(num) %2 == 0:
        sum_num += int(num)

print(sum_num)
