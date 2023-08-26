cache = {}


def dec_cache(func):
    def wrapper(*args):
        if args in cache:
            print('Such function parameters are present in the cache and taken from it!')
            # print(cache)
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            print('Such function parameters are not present in the cache. The result has been calculated!')
            # print(cache)
            return result
    return wrapper

@dec_cache
def sum(a, b):
     return a + b


print(sum(1, 2))
print(sum(1, 2))
print(sum(3, 4))
print(sum(1, 8))
print(sum(1, 8))



