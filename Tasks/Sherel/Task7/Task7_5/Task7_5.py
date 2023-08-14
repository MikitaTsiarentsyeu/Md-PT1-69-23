import json

def open_file_for_read(file_path, metod):
    with open(file_path, metod) as file:
        data = json.load(file)
        return data

def find_value_to_json_file(key, file_path):
    data = open_file_for_read(file_path, metod="r")
    def find(d, key):
        if key in d:
            return d[key]
        for k, v in d.items():
            if isinstance(v, dict):
                result = find(v, key)
                if result:
                    return result
    return find(data, key)

def add_key_value_to_json_file(file_path, key, key_change, value):
    data = open_file_for_read(file_path, metod="r")
    data[key] = value
    data[key_change] = value
    with open(file_path, 'w') as file:
        json.dump(data, file, sort_keys=True, indent=4)

while True:
    try:
        file_path = 'Task7_5-logs.json'
        a = input('Enter the first value: ')
        b = input('Enter the second value: ')
        value = int(a) + int(b)
        key = '({}, {})'.format(a, b)
        key_change = '({}, {})'.format(b, a)
        result = find_value_to_json_file(key, file_path)
        if result != None:
            print('The sum of arguments {} and {} is equal {} (CASH)'.format(a, b, result))
        elif result is None:
            add_key_value_to_json_file(file_path, key, key_change, value)
            print('The sum of arguments {} and {} is equal {} (Online)'.format(a, b, value))
    except:
        print('Enter integer value for argument "a" and "b"')