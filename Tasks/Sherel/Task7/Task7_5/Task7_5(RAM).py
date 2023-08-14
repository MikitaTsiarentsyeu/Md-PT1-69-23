my_dict = dict()

def find_value_to_my_dict(key, my_dict):
    """
    Recursive function cache key lookup
    :return: key/value or None
    """
    if key in my_dict:
        return my_dict[key]
    for value in my_dict.values():
        if isinstance(value, dict):
            result = find_value_to_my_dict(key, value)
            if result:
                return result

def add_in_dict(key, value):
    """
    Function to group required parameters before writing them to my dict
    :param key: '(a, b)'
    :param value: summ a and b
    :return: updated dictionary with new key and value
    """
    my_dict[key] = value
    return my_dict

while True:
    try:
        a = input('Enter the first value: ')
        b = input('Enter the second value: ')
        value = int(a) + int(b)
        key = '({}, {})'.format(a, b)
        result = find_value_to_my_dict(key, my_dict)
        if result is not None:
            print('The sum of arguments {} and {} is equal {} (Cache)'.format(a, b, result))
        else:
            add_in_dict(key, value)
            print('The sum of arguments {} and {} is equal {} (Online)'.format(a, b, value))
    except ValueError:
        print('Enter integer value for argument "a" and "b"')