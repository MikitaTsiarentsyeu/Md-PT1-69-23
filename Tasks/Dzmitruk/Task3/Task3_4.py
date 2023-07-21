# a program that takes a list of numbers as input
# and returns the second largest number in the list

list_of_num = input("Pleese, input a list of numbers: ")

list_of_num = set(list(list_of_num.split(", ")))

numbers = []

for num in list_of_num:
    num = int(num)
    numbers.append(num)
    
max_num = numbers[0]
second_largest_num = float("-inf")

if len(numbers) == 1:
    print("The second largest number in the list is not defined.")
    exit()

for num in numbers:
    if num > max_num:
        second_largest_num = max_num
        max_num = num
    elif num > second_largest_num and num != max_num:
        second_largest_num = num

print("The second largest number in the list is -", second_largest_num)



    
    
