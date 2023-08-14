import json

def open_file_for_read(file_path):
    """
    Function to open json file (for reuse without cloning)
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def find_value_to_json_file(key, data):
    """
    Recursive function cache key lookup
    :return: key/value or None
    """
    if key in data:
        return data[key]
    for value in data.values():
        if isinstance(value, dict):
            result = find_value_to_json_file(key, value)
            if result:
                return result


def add_key_value_to_json_file(data, key, key_change, value):
    """
    Function to group required parameters before writing them to cache
    :param data: is open file for read
    :param key: '(a, b)'
    :param key_change: '(b, a)'
    :param value: summ a and b
    """
    data[key] = value
    data[key_change] = value


def main():
    """
    Sum function of two integers
    :return: the result of the calculation - made in real time (if not in the cache) or will return the value from
    the cache and will not perform the calculation
    """
    while True:
        try:
            file_path = 'Task7_5-logs.json'
            a = input('Enter the first value: ')
            b = input('Enter the second value: ')
            value = int(a) + int(b)
            key = '({}, {})'.format(a, b)
            key_change = '({}, {})'.format(b, a)

            data = open_file_for_read(file_path)

            result = find_value_to_json_file(key, data)
            if result is not None:
                print('The sum of arguments {} and {} is equal {} (CASH)'.format(a, b, result))
            else:
                add_key_value_to_json_file(data, key, key_change, value)
                with open(file_path, 'w') as file:
                    json.dump(data, file, sort_keys=True, indent=4)
                print('The sum of arguments {} and {} is equal {} (Online)'.format(a, b, value))
        except ValueError:
            print('Enter integer value for argument "a" and "b"')


if __name__ == '__main__':
    main()