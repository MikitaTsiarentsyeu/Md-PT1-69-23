""""""

import json
file_path = 'cache.json'

def cache(func):
    def wrapper(*args, **kwargs):
        key = '{}'.format(args)
        with open(file_path, 'r') as file:
            data = json.load(file)
        if key in data:
            return print('Cache', data[key])
        else:
            result = func(*args, **kwargs)
            data[key] = result
            with open(file_path, 'w') as file:
                json.dump(data, file, sort_keys=True, indent=4)

            return print('Online:', data[key])
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