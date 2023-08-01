from functools import reduce


def sum_two_integers(*args: int) -> int:
    # Check if any arguments are provided
    if not args:
        raise ValueError(
            'No arguments provided. Please provide at least two integers.')

    # Check if all arguments are integers
    if not all(isinstance(arg, int) for arg in args):
        invalid_args = [str(arg) for arg in args if not isinstance(arg, int)]
        raise TypeError(
            f'Invalid arguments: {", ".join(invalid_args)}. All arguments must'
            'be integers.')

    # Calculate the sum using the reduce function
    return reduce(lambda x, y: x + y, args)


test_cases = [
    [5, 6],
    [-3, 8],
    [10, 20],
    [0, 0],
    [100, 200],
    [5, '6'],
    [5.5, 6.6],
    [],
]

for numbers in test_cases:
    try:
        result = sum_two_integers(*numbers)
        print(f'The sum of {numbers[0]} and {numbers[1]} is equal to {result}')
    except ValueError as ve:
        print(f'Error: {ve}')
    except TypeError as te:
        print(f'Error: {te}')
