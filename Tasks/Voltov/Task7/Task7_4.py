# Write a decorator function that logs the
# execution time, arguments and return value
# of a function to a file.

import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        with open('log.txt', 'a') as f:
            f.write(f"Function {func.__name__} was called with arguments {args}, {kwargs} and returned {result}. Execution time: {end_time - start_time} seconds.\n")
        return result
    return wrapper
