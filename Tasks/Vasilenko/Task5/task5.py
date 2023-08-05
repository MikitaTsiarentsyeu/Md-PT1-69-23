"""task 5_1
Write a function that takes two integers as arguments and returns their sum"""


def sum_expression(a, b):
    res = a + b
    return res


print(sum_expression(34, 43))

"""task 5_2
Write a function that takes a list of strings as an argument 
and returns a new list of strings that are all reversed"""


def reversed_strings(input_list):
    reversed_list = []
    for string in input_list:
        new_string = string[::-1]
        reversed_list.append(new_string)
    return reversed_list


print(reversed_strings(['olleh', 'ym', 'raed', 'dneirf']))

"""task 5_3
Write a function that takes a list of strings as an argument 
and returns a new list with all the strings that have a length greater than 5"""


def more_than_5(input_list):
    result = []
    for string in input_list:
        if len(string) > 5:
            result.append(string)
        else:
            continue
    return result


print(more_than_5(['London', 'is', 'the', 'capitol', 'of', 'Great', 'Britain']))

"""task 5_4
Write a function that takes a string as an argument and returns two numbers, 
first for count of lower case symbols, 
second for count of the upper case symbols in the initial string"""


def lower_upper_count(string):
    lower_count = 0
    upper_count = 0
    for elem in string:
        if elem.islower():
            lower_count += 1
        elif elem.isupper():
            upper_count += 1
        else:
            continue
    return lower_count, upper_count


print(lower_upper_count('ThiS IS a coMPLetElY NoRMaL teXT!'))

"""task5_5
Write a function that takes an ordered list of numbers without duplicates 
and returns a string with ranges for those numbers"""


def get_ranges(numbers):
    ranges = []
    start_range = numbers[0]
    end_range = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] != 1 and start_range == end_range:
            ranges.append(str(start_range))
            start_range = numbers[i]
        elif numbers[i] - numbers[i - 1] != 1 and start_range != end_range:
            ranges.append(f'{start_range}-{end_range}')
            start_range = numbers[i]
            end_range = numbers[i]
        elif numbers[i] - numbers[i-1] == 1:
            end_range = numbers[i]

    if end_range == numbers[-1] and end_range == start_range:
        ranges.append(str(start_range))
    elif end_range == numbers[-1] and end_range != start_range:
        ranges.append(f'{start_range}-{end_range}')

    ranges_str = ','.join(ranges)
    return ranges_str


print(get_ranges([1, 3, 4, 5, 7, 8, 10, 11, 14, 17, 18, 19, 21, 22, 25, 28, 29, 31, 32]))
