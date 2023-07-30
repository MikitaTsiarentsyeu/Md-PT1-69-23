"""4. Write a program that takes a list of numbers as input and returns the second largest number in the list."""

user_input = input("Enter your list of numbers separated by a space:\n")
user_input = user_input.split()

first_largest = int(user_input[0])
second_largest = int(user_input[0])

for num in user_input:
    if int(num) > first_largest:
        second_largest = first_largest
        first_largest = int(num)
    elif int(num) > second_largest and int(num) != first_largest:
        second_largest = int(num)

print("The second largest number in the list:", second_largest)