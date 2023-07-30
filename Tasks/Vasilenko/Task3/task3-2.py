"""Write a program that takes a list of numbers as input
and returns the sum of all even numbers in the list"""

print("Here you can calculate the sum of all even numbers you input")

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

sum_ev = 0
for e in num_list:
    while e % 2 == 0:
        sum_ev += e
        break
print(f'The sum of your even numbers is {sum_ev}')
