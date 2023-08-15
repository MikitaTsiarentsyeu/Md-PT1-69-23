"""this is the simplest example that I could squeeze out of my finger to create a decorator,
the cache is crunched throughout the program, as soon as the program stops the dict is emptied"""

my_dict = dict()

def cache(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        key = '{}'.format(args)
        if key in my_dict:
            return print('Cash', my_dict[key])
        else:
            my_dict[key] = result
            return print('Online:', my_dict[key])
        return result
    return wrapper

@cache
def summ(x, y):
    return x + y

while True:
    try:
        summ(int(input('a: ')), int(input('b: ')))
    except:
        print('oops')