"""task 7-5. Write a decorator function that caches the return value of a function with a dictionary.
If the function is called again with the same arguments, return the cached value instead of computing it again."""

def caching_results(function):
    cached_results = {}
    def wrapper(*args):
        sorted_arguments = sorted(args)
        key_sorted_arguments = tuple(sorted_arguments)
        if key_sorted_arguments in cached_results:
            print(f'The result is {cached_results[key_sorted_arguments]} (and is taken from cache)')
        else:
            result = function(*args)
            cached_results[key_sorted_arguments] = result
            return print(f'The result is {result}')
    return wrapper


@caching_results
def sum_function(*args):
    try:
        result = 0
        for number in args:
            result += number

        return result

    except TypeError:
        print("Invalid input type")


sum_function(2, 3)
sum_function(4, 5)
sum_function(3, 2)
sum_function(4, 5)
