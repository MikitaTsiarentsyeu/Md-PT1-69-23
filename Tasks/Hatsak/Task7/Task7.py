def div(a, b):
    """1. Write a function that takes two numbers as input and returns their division.
     Handle the ZeroDivisionError and return "Cannot divide by zero" if the denominator is zero.
    """
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def open_file(file_name):
    """2. Write a function that reads a file and returns its contents as a string.
     Handle the FileNotFoundError and return "File not found" if the file does not exist.
    """
    try:
        f = open(file_name, mode='r')
        print(f.read())
        f.close()
        return 'File closed'
    except FileNotFoundError:
        return 'File not found'


def sum_nums(nums):
    """3. Write a function that takes a list of integers as input and
     returns the sum of all even numbers in the list.
      Handle the TypeError and return "Invalid input type"
      if the input is not a list or not every element is int.
    """

    try:
        if all(isinstance(x, int) for x in nums):
            return sum(nums)
        else:
            raise TypeError
    except TypeError:
        return 'Invalid input type'

def tests():
    assert sum_nums([1, 2]) == 3
    assert sum_nums([1, '2']) == 'Invalid input type'
    assert sum_nums([1, 1.1]) == 'Invalid input type'
    assert sum_nums('1,2') == 'Invalid input type'
    assert sum_nums(1) == 'Invalid input type'


tests()

import time
def info(func):
    """4. Write a decorator function that logs the execution time,
     arguments and return value of a function to a file.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения функции {end_time - start_time} секунд')
        return value
    return wrapper

def cache(func):
    """5. Write a decorator function that caches the return value of a function with a dictionary.
    If the function is called again with the same arguments,
    return the cached value instead of computing it again."""
    collection = {}
    def wrapper(*args, **kwargs):
        if (*args, *kwargs.values()) in collection:
            return collection[(*args, *kwargs.values())]
        val = func(*args, **kwargs)
        collection[*args, *kwargs.values()] = val
        return val
    return wrapper