from string import punctuation


# task5_1
def sum(a, b):
    return a + b


# task5_2
def reversed_strings(strings):
    new_strings = []
    for string in strings:
        string = ''.join(reversed(string))
        new_strings.append(string)
    return new_strings


# task5_3
def long_strings(strings):
    new_list = []
    for string in strings:
        if len(string) > 5:
            new_list.append(string)
    return new_list


# task5_4
def lower_upper_count(string):
    lower_count, upper_count = 0, 0
    for char in string:
        if char in punctuation or char == " ":
            continue
        if char.islower():
            lower_count += 1
        else:
            upper_count += 1
    return lower_count, upper_count


# task5_5
def get_ranges(numbers):
    ranges_dict = {}
    range_order = 0
    ranges_dict[range_order] = [(numbers[0])]
    previous_number = numbers[0]
    for number in numbers[1:]:
        if number != previous_number + 1:
            range_order += 1
            ranges_dict[range_order] = []
        ranges_dict[range_order].append(number)
        previous_number = number
    ranges = []
    for order in ranges_dict.values():
        if len(order) == 1:
            range_string = f"{order[0]}"
        else:
            range_string = f"{order[0]}-{order[len(order)-1]}"
        ranges.append(range_string)
    return ", ".join(string for string in ranges)


with open("Task 5.txt", "r", encoding="UTF-8") as file:
    text = file.read()
text = text.split("\n\n")
for task_order in range(len(text)):
    print(text[task_order].strip())

    if task_order == 0:
        a, b = 2, 3
        print(f"Sum of {a} and {b} is {sum(a, b)}")

    elif task_order == 1:
        list_of_strings = ["Hello world", "    of", "happiness", "oops"]
        print(f"Original list: {list_of_strings}")
        list_of_strings = reversed_strings(list_of_strings)
        print(f"New list: {list_of_strings}")

    elif task_order == 2:
        list_of_strings = ["Hello", "     a", "world of happiness", "oops",
                           "and this task is done"]
        print(f"Original list: {list_of_strings}")
        list_of_strings = long_strings(list_of_strings)
        print(f"New list: {list_of_strings}")

    elif task_order == 3:
        line = "YooOoo, what's up? I hoPe yoU diD wEll, hEHe"
        print(line)
        lower, upper = lower_upper_count(line)
        print(f"lower case symbols - {lower}\nupper case symbols - {upper}")

    else:
        nums = [2, 3, 4, 8, 11, 12, 22]
        print()
        print(f"get_ranges({nums})  -> \"{get_ranges(nums)}\"")

    print()
