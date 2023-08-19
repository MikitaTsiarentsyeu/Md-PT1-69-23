"""task 7-3. Write a function that takes a list of integers as input and returns the sum of all even numbers in the list.
Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int."""


def sum_of_even_numbers(list_of_numbers):
    try:
        result = 0
        for number in list_of_numbers:
            if number % 2 == 0:
                result += number
            else:
                continue
        return print(f'The sum of even numbers is {result}')

    except TypeError:
        print("Invalid input type")


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_list2 = [1, 2, 3, 4, 5, 6, 'qwerty']
test_list3 = 'qwerty'

sum_of_even_numbers(test_list)
sum_of_even_numbers(test_list2)
sum_of_even_numbers(test_list3)
