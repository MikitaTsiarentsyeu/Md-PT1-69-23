def division_of_numbers(a: float, b: float) -> float:
    """
    A function that takes two numbers as input and returns their division. Handle the ZeroDivisionError
    and return "Cannot divide by zero" if the denominator is zero.
    :param a: integer or float numbers
    :param b: integer or float numbers
    :return try: dividing number A by B
    :return except: 'Cannot divide by zero' or other error.
    """
    try:
        return print(a/b)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except:
        print('Other error')

division_of_numbers(6, 0)          # Otput: Cannot divide by zero
# division_of_numbers(6, '0')        # Otput: Other error
# division_of_numbers(6, 3)          # Otput: 2.0


def read_file():
    """
    A function that reads a file and returns its contents as a string. Handle the FileNotFoundError
    and return "File not found" if the file does not exist.
    :return try: text in the file
    :return except: 'File not found' or other error.
    """
    try:
        with open("fileName.py", 'r') as f:
            return print(f.read())
    except FileNotFoundError:
        print('File not found')
    except:
        print('Other error')

read_file()


def sum_integers_in_list(szList: list) -> int:
    """
    A function that takes a list of integers as input and returns the sum of all even numbers in the list.
    Handle the TypeError and return "Invalid input type" if the input is not a list or not every element is int.
    :param szList: list only integers
    :return: summ integers in list
    """
    try:
        return print(sum([integer for integer in szList if integer % 2 == 0]))
    except TypeError:
        print('Invalid input type')
    except:
        print('Other error')

szList = 1,2,3,4,5,6,7,8.1,9,10
sum_integers_in_list(szList)