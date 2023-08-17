print("""This program performs the addition of 2 value and has a decorator function that caches the return value of the
function with a dictionary. If the function is called again with the same arguments, 
it returns the cached value rather than recalculating it.""")

my_dict = dict()  # cache - dictionary

def cache(func):
    """
    A decorator function that caches the return value of a function with a dictionary.
    :param func: def summ(x, y)
    """
    def wrapper(*args, **kwargs):
        """
        :param args: first and second input value
        :return: the result of the sum function,if the calculation has already been made - returns the result from cache
        """
        key = '{}'.format(args)
        if key in my_dict:
            return print('Cache', my_dict[key])
        else:
            result = func(*args, **kwargs)
            my_dict[key] = result
            return print('Online:', my_dict[key])
    return wrapper

@cache
def summ(x, y):
    """
    Func summ values input first and second
    :param x: first input
    :param y: second input
    """
    return x + y

while True:
    try:
        summ(int(input('Enter your first integer value: ')), int(input('Enter your second integer value: ')))
    except:
        print('Unknown error or program terminated.')