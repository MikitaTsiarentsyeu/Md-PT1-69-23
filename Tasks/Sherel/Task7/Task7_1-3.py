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
            print(f.read())
    except FileNotFoundError:
        print('File not found')
    except:
        print('Other error')

read_file()


def