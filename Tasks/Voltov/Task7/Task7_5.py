# Write a decorator function that caches
# the return value of a function with a
# dictionary. If the function is called again
# with the same arguments, return the cached
# value instead of computing it again.

def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper