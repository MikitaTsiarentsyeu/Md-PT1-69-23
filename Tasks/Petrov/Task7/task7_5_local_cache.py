from decimal import Decimal, InvalidOperation

# dictionary for all functions, that will be cached
caches = {}


def caching(func):
    """Decorator function that caches the return value of a function
    with a dictionary

    func
        function that will be decorated"""

    # Creating individual dictionary for certain function,
    # that will be cached
    caches[func.__name__] = {}
    cache_current = caches[func.__name__]

    def wrapper(list):
        arguments = tuple(sorted(list))
        # If the function is called again with the same arguments,
        # return the cached value instead of computing it again.
        if arguments in cache_current:
            print("Result was taken from cache")
        else:
            cache_current[arguments] = func(list)
        return cache_current[arguments]
    return wrapper


@caching
def args_sum(numbers_list):
    """Return sum of all numbers from the given."""
    try:
        return sum(Decimal(i) for i in numbers_list)
    except InvalidOperation:
        # If input can't be converted to Decimal, InvalidOperation raises
        return "Error, wrong input(s)"


while True:
    print("Input numbers to sum, none to exit:", end=" ")
    numbers = [_ for _ in input().split()]
    if numbers:
        print(f"Sum of your input: {args_sum(numbers)}")
    else:
        break
