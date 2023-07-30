"""10. Write a program that takes a list of numbers as input and returns the largest prime number in the list."""

user_input = input("Enter your list of numbers separated by a space:\n")
user_input = user_input.split()

#check input the largest prime number and creat the list.
myList = []
for x in user_input:
    rubilnik = True
    if int(x) <= 1:
        continue
    for i in range(2, int(int(x) ** 0.5) + 1):
        if int(x) % i == 0:
            rubilnik = False
            break
    if rubilnik is True:
        myList.append(x)
#print(myList)

#check max number in list option 1
#max_number_p = max(myList, key=int)

#check max number in list option 2
max_number_p = 0
for i in myList:
    if int(i) > int(max_number_p):
        max_number_p = i

print(max_number_p)