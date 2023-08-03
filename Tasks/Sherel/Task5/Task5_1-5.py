#1. Write a function that takes two integers as arguments and returns their sum.

def sum_of_numbers(a, b):
    """
    :param a: first argument -> integer
    :param b: second argument -> integer
    :return: sum arguments
    """
    if a == str(a) or b == str(b):
        print('Please, enter only integer value...')
    else:
        return a + b

result = sum_of_numbers('20', 6.5)
print('' if result is None else result)
# Input (20, 6.5)        # Input ('20', 6.5)
# Output: 26.5           # Output: 'Please, enter only integer value...'


#2. Write a function that takes a list of strings as an argument and
# returns a new list of strings that are all reversed.

input_list_2 = ["Hi", "my", "name", "is", "Artyom", "Sherel"]

def reverse_strings_in_list(input_list_2):
    """
    :param input_list_2: a list of strings as an argument
    :return: a new list of strings that are all reversed
    """
    reversed_list = [string[::-1] for string in input_list_2[::-1]]
    return reversed_list

print(reverse_strings_in_list(input_list_2))
# Output: ['lerehS', 'moytrA', 'si', 'eman', 'ym', 'iH']


# 3. Write a function that takes a list of strings as an argument and
# returns a new list with all the strings that have a length greater than 5.

input_list_3 = ["London", ",", "is", "the", "capital", "of", "Great", "Britain",
                ",", "its", "political", ",", "economic", "and", "cultural", "centre", "."]

def filter_strings_by_length(input_list_3):
    """
    :param input_list_3: a list of strings as an argument
    :return: a new list with all the strings that have a length greater than 5
    """
    return [string for string in input_list_3 if len(string) > 5]

print(filter_strings_by_length(input_list_3))
# Output: ['London', 'capital', 'Britain', 'political', 'economic', 'cultural', 'centre']


# 4. Write a function that takes a string as an argument and returns two numbers,
# first for count of lower case symbols, second for count of the upper case symbols in the initial string.

initial_string = "London is the capital of Great Britain, its political, economic and cultural centre."

def count_lower_upper_case_symbols(initial_string):
    """
    :param initial_string: a string as an argument
    :return: two numbers, first for count of lower case symbols, second for count of the upper case symbols
    """
    #the second variant, by Romanychev
    count_lower = len([char for char in initial_string if char.islower()])
    count_upper = len([char for char in initial_string if char.isupper()])

    #the firs variant
    # count_lower = 0
    # count_upper = 0
    # for char in initial_string:
    #     if char.islower():
    #         count_lower += 1
    #     elif char.isupper():
    #         count_upper += 1

    return count_lower, count_upper

lower_count, upper_count = count_lower_upper_case_symbols(initial_string)

print(f"""Count lower case symbols: {lower_count}\nCount upper case symbols: {upper_count}""")
# Output: Count lower case symbols: 66
#         Count upper case symbols: 3


# 5. Write a function that takes an ordered list of numbers without duplicates
# and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

numbers = [23, -9, 0, 21, 1, 1, -13, 1, 1, 3, 2, 8, 6, 5, 10, 11, 12, 15, 22]

def string_with_ranges(numbers):
    """
    :param numbers: an ordered list of numbers without duplicates
    :return: a string with ranges for those numbers
    """
    numbers = list(set(numbers)) # cleaning up duplicates
    numbers.sort() # ordered list
    ranges = []
    start_range = end_range = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] == end_range + 1:
            end_range = numbers[i]
        else:
            if start_range == end_range:
                ranges.append(str(start_range))
            else:
                ranges.append(f"{start_range}-{end_range}")
            start_range = end_range = numbers[i]
    if start_range == end_range:
        ranges.append(str(start_range))
    else:
        ranges.append(f"{start_range}-{end_range}")

    return '"' + ", ".join(ranges) + '"'
print(string_with_ranges(numbers), type(string_with_ranges(numbers)))
# Output: "-13, -9, 0-3, 5-6, 8, 10-12, 15, 21-23" <class 'str'>

#or
#     return ", ".join(ranges)
# print(f'''"{string_with_ranges(numbers)}"''', type(string_with_ranges(numbers)))
# Output: "-13, -9, 0-3, 5-6, 8, 10-12, 15, 21-23" <class 'str'>
