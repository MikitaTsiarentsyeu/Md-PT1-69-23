def cache(func):
    storage = {}
    def wrapper(*args):
        if args in storage:
            res = storage[args]
        else:
            res = func(*args)
            storage[args] = res
        return res
        
    return wrapper

@cache
def sum(a, b):
    return a+b

@cache
def mult(a, b):
    return a*b

sum(2, 3)
mult(2, 3)