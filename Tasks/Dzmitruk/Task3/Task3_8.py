# a program that takes a list of numbers as input and returns
# the average of all numbers in the list.

numbers = input("Please, input a list of number: ")
numbers = list(numbers.split(", "))

s = 0

for number in numbers:
    number = int(number)
    s = s + number
    average = s/len(numbers)

print("The average of all numbers in the list is: ", average)







