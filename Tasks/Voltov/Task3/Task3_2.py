# 2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.


user_input = input("Enter a list of numbers separated by commas: ")
num_list = user_input.split(",")
even_sum = 0
for num in num_list:
    num = int(num)
    if num % 2 == 0:
        even_sum += num
print("The sum of the even numbers in the list:", even_sum)