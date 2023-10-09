def decorator(func):
    collection = {}
    def inner(*args, **kwargs):
        if (*args, *kwargs.values()) in collection:
            return collection[(*args, *kwargs.values())]
        val = func(*args, **kwargs)
        collection[*args, *kwargs.values()] = val
        return val
    return inner