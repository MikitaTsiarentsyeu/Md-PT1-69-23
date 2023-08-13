def division_of_numbers(a: float, b: float) -> float:
    """
    a function that takes two numbers as input and returns their division. Handle the ZeroDivisionError
    and return "Cannot divide by zero" if the denominator is zero.
    :param a: integer or float numbers
    :param b: integer or float numbers
    :return: dividing number A by B
    """
    try:
        return print(a/b)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except:
        print('Other error')

division_of_numbers(6, 0)          # Otput: Cannot divide by zero
division_of_numbers(6, '0')        # Otput: Other error
division_of_numbers(6, 3)          # Otput: 2.0