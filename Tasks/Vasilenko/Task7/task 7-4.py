"""task 7-4. Write a decorator function that logs the execution time,
arguments and return value of a function to a file."""

import time

def funtion_info(function):
    def wrapper(*args):
        start_time = time.time()
        result = function(*args)
        finish_time = time.time()
        execution_time = finish_time - start_time

        with open("task 7-4.txt", "w") as file:
            file.write(f'The information about {function.__name__} function is as follows:\nThe execution time is {execution_time}\nThe arguments of the function are {args}\nThe result of the function is {result}')

        return result
    return wrapper


@funtion_info
def multiplication(*args):
    try:
        result = 1
        for number in args:
            result *= number
        return result

    except TypeError:
        print("Invalid input type")


multiplication(1, 2, 3, 34, 21, 16, 324, 512, 999, 1231, 7264, 8364, 1123, 8232, 8364, 9164, 1111)
