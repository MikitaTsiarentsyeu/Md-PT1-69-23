# 1.Write a function that takes two integers as arguments and returns their sum.

def sum_numbers(a, b):
    return a + b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The sum of the numbers is:", sum_numbers(a, b))


# 2.Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.

def reverse_strings(strings):
    reversed_list = []
    for string in strings:
        reversed_list.append(string[::-1])
    return reversed_list
strings = input("Enter a list of strings separated by commas: ").split(", ")
print("Reversed lines:", reverse_strings(strings))

# 3.Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

def filter_long_strings(strings):
    filtered_list = []
    for string in strings:
        if len(string) > 5:
            filtered_list.append(string)
    return filtered_list
strings = input("Enter a list of strings separated by commas: ").split(", ")
print("Lines longer than 5 characters:", filter_long_strings(strings))


# 4.Write a function that takes a string as an argument and returns two numbers, first for
# count of lower case symbols, second for count of the upper case symbols in the initial string.

def count_case(string):
    lower_count = 0
    upper_count = 0
    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    return lower_count, upper_count
string = input("Enter the string: ")
lower_count, upper_count = count_case(string)
print("Number of characters in lower case:", lower_count)
print("Number of characters in upper case:", upper_count)


# 5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

def get_ranges(numbers):
    ranges = []
    start = end = numbers[0]
    for num in numbers[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "-" + str(end))
            start = num
            end = num
    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(str(start) + "-" + str(end))
    return ", ".join(ranges)

numbers = list(map(int, input("Enter a list of numbers separated by commas: ").split(",")))
print("Number ranges:", get_ranges(sorted(numbers)))