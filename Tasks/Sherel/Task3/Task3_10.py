"""10. Write a program that takes a list of numbers as input and returns the largest prime number in the list."""

user_input = input("Enter your list of numbers separated by a space:\n")
user_input = user_input.split()

#check input the largest prime number and creat the list.
miList = []
for num in user_input:
    rubilnik = True
    if int(num) <= 1:
        continue
    for i in range(2, int(int(num) ** 0.5) + 1):
        if int(num) % i == 0:
            rubilnik = False
            break
    if rubilnik is True:
        miList.append(num)
#print(miList)

#check largest int in creat list 'mtList'
max_number_p = 0
for i in miList:
    if int(i) > int(max_number_p):
        max_number_p = i

print(max_number_p)
