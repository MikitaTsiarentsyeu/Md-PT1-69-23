"""
How the program works: I open a json file - which stores the history of my calculations in the long run
(if the file is missing, I create an empty one) and take the entire history from it into my temporary dictionary,
which will act as my short-term cache, since reading file consumes more PC resources than its one-time iteration.
If my new calculation is not in my dictionary stored in memory, I add to ram and add cache to json,
while all subsequent calculations are checked only by ram memory so as not to constantly open json for reading,
but only write to it.
"""
import json

file_path = 'cache.json'
try:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
except:
    with open(file_path, 'w') as json_file:
        json.dump({}, json_file)

def write_in_json():
    with open(file_path, 'w') as file:
        json.dump(data, file, sort_keys=True, indent=4)

def cache(func):
    def wrapper(*args, **kwargs):
        key = '{}'.format(args)
        if key in data:
            return print('Cache result:', data[key])
        else:
            result = func(*args, **kwargs)
            data[key] = result
            write_in_json()
            return print('Online result:', data[key])
    return wrapper

@cache
def summ(x, y):
    return x + y

while True:
    try:
        summ(int(input('Enter your first integer value: ')), int(input('Enter your second integer value: ')))
    except:
        print('Unknown error or program terminated.')