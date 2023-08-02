#1. Write a function that takes two integers as arguments and returns their sum.

def sum_of_numbers(a, b):
    return a + b

result = sum_of_numbers(-20, 6)
print(result)
# Output: -14


#2. Write a function that takes a list of strings as an argument and
# returns a new list of strings that are all reversed.

input_list_2 = ["Hi", "my", "name", "is", "Artyom", "Sherel"]

def reverse_strings_in_list(input_list_2):
    reversed_list = []
    for string in input_list_2[::-1]:
        reversed_string = string[::-1]
        reversed_list.append(reversed_string)
    return reversed_list

print(reverse_strings_in_list(input_list_2))
# Output: ['lerehS', 'moytrA', 'si', 'eman', 'ym', 'iH']


# 3. Write a function that takes a list of strings as an argument and
# returns a new list with all the strings that have a length greater than 5.

input_list_3 = ["London", ",", "is", "the", "capital", "of", "Great", "Britain",
                ",", "its", "political", ",", "economic", "and", "cultural", "centre", "."]

def filter_strings_by_length(input_list_3):
    return [string for string in input_list_3 if len(string) > 5]

print(filter_strings_by_length(input_list_3))
# Output: ['London', 'capital', 'Britain', 'political', 'economic', 'cultural', 'centre']


# 4. Write a function that takes a string as an argument and returns two numbers,
# first for count of lower case symbols, second for count of the upper case symbols in the initial string.

initial_string = "London is the capital of Great Britain, its political, economic and cultural centre."

def count_lower_upper_case_symbols(initial_string):
    count_lower = 0
    count_upper = 0

    for char in initial_string:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1

    return count_lower, count_upper

lower_count, upper_count = count_lower_upper_case_symbols(initial_string)

print(f"""Count lower case symbols: {lower_count}\nCount upper case symbols: {upper_count}""")
# Output:
# Count lower case symbols: 66
# Count upper case symbols: 3
