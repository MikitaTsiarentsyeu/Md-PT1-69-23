from decimal import Decimal, InvalidOperation


caches = {}


def caching(func):

    caches[func.__name__] = {}
    cache_current = caches[func.__name__]

    def wrapper(list):
        arguments = tuple(sorted(list))
        if arguments in cache_current:
            print("Result was taken from cache")
        else:
            cache_current[arguments] = func(list)
        return cache_current[arguments]
    return wrapper


@caching
def args_sum(numbers_list):
    try:
        return sum(Decimal(i) for i in numbers_list)
    except InvalidOperation:
        return "Error, wrong input(s)"


while True:
    print("Input numbers to sum, none to exit:", end=" ")
    numbers = [_ for _ in input().split()]
    if numbers:
        print(f"Sum of your input: {args_sum(numbers)}")
    else:
        break
