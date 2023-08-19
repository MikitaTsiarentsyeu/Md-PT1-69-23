
cache_dict = dict()

def cache(funk):
    """
    a decorator function that caches the return value of a function 
    with a dictionary. If the function is called again with the same
    arguments, return the cached value instead of computing it again.
    """
    def wrapper(*args):         
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = funk(*args)
            cache_dict[args] = result 
        return result
    return wrapper
        
@cache    
def sum_num(x, y):
    return x+y
