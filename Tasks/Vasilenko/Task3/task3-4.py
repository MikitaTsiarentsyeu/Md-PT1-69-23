"""Write a program that takes a list of numbers as input
and returns the second largest number in the list"""

print("Here you can find out the second largest number in your list of numbers")

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

max1 = num_list[0]
for e in num_list:
    if e > max1:
        max1 = e

max2 = num_list[0]
for e in num_list:
    if e > max2 and e != max1:
        max2 = e

print(f'The second largest number in your list is {max2}')
