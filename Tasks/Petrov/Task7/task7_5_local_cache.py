from decimal import Decimal, InvalidOperation


cache = {}


def caching(func):
    def wrapper(list):
        arguments = tuple(sorted(list))
        if arguments in cache:
            print("Result was taken from cache")
        else:
            cache[arguments] = func(list)
        return cache[arguments]
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
