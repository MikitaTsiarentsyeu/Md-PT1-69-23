"""Write a program that takes a list of numbers as input and
returns the largest prime number in the list"""

print("Here you can find out the largest of the prime numbers in your list")

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

prime_list = []

for elem in num_list:
    if elem < 2:
        continue
    count = 0
    divider = 2
    while divider < elem:
        if elem % divider == 0:
            count += 1
        divider += 1
    if count == 0:
        prime_list.append(elem)

max1 = prime_list[0]
for e in prime_list:
    if e > max1:
        max1 = e


print(f'The largest of the prime numbers in your list is {max1}')
