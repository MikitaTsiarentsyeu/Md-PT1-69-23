from decimal import Decimal, InvalidOperation
import json

caches = {}


def caching(func):

    try:
        current_cache = f"{func.__name__}_cache.json"
        file = open(current_cache, "r", encoding="UTF-8")
    except FileNotFoundError:
        file = open(current_cache, "w+", encoding="UTF-8")
        json.dump({}, file)
        file.seek(0)

    caches[func.__name__] = json.load(file)
    current_cache = caches[func.__name__]
    file.close

    def wrapper(list):
        arguments = str(sorted(list))
        if arguments in current_cache:
            print("Result was taken from cache")
        else:
            current_cache[arguments] = str(func(list))
        return current_cache[arguments]
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


for key, value in caches.items():
    file_name = f"{key}_cache.json"
    file = open(file_name, "w", encoding="UTF-8")
    json.dump(value, file, indent=4)
    file.close
