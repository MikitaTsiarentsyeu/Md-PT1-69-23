"""Write a program that takes a list of numbers as input and
returns the average of all numbers in the list"""

print("Here you can find out the average of the numbers in your list")

numbers = (input("Please, enter the numbers(n1 n2 n3 etc.):\n"))
numbers = list(numbers.split(' '))

num_list = []

for i in numbers:
    if not i.isdigit():
        print("Wrong input. Please, enter only integer numbers")
        exit()
    else:
        i = int(i)
        num_list.append(i)

sum_all = 0
for e in num_list:
    sum_all += e

average = sum_all/len(num_list)
average = round(average, 2)

print(f'The average of the numbers in your list is {average}')
