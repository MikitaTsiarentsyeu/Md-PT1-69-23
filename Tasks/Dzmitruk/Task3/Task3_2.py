# a program that takes a list of numbers as input
# and returns the sum of all even numbers in the list

list_of_num = input("Pleese, input a list of numbers: ")

list_of_num = list(list_of_num.split(", "))

sum_of_num = 0

for num in list_of_num:
    num = int(num)
    if num % 2 == 0:
        sum_of_num += num

print("The sum of all even numbers in the list is - ", sum_of_num)



    
    
