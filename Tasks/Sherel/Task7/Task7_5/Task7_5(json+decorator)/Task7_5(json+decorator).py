import json

print("""This program performs the addition of 2 value and has a decorator function that caches the return value of the
function with a dictionary. If the function is called again with the same arguments, 
it returns the cached value rather than recalculating it.
P.S. cache is stored in a json file and is available when the program is restarted.""")

file_path = 'cache.json' #file cache

def cache(func):
    """
    A decorator function that caches the return value of a function with a dictionary.
    :param func: def summ(x, y)
    """
    def wrapper(*args, **kwargs):
        """
        :param args: first and second input value
        :return: the result of the sum function, if the calculation has already been made returns the result from
         cache in json file "cache.json"
        """
        key = '{}'.format(args)
        with open(file_path, 'r') as file:
            data = json.load(file)
        if key in data:
            return print('Cache result:', data[key])
        else:
            result = func(*args, **kwargs)
            data[key] = result
            with open(file_path, 'w') as file:
                json.dump(data, file, sort_keys=True, indent=4)
            return print('Online result:', data[key])
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
    except FileNotFoundError: #if the cache file is not found in the project folder - create a file
        with open(file_path, 'w') as json_file:
            json.dump({}, json_file)
    except:
        print('Unknown error or program terminated.')