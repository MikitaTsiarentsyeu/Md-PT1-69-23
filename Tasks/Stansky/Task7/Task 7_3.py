def sum_even(list_numbers):
    sum_ev = 0
    try:
        if not isinstance(list_numbers, list):
            raise TypeError
        for element in list_numbers:
            if not isinstance(element, int):
                raise TypeError
            else:
                if element % 2 == 0:
                    sum_ev += element
        return sum_ev

    except TypeError:
        return "Invalid input type"


print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]))
print(sum_even([1, 2.55, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_even((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(sum_even('andrew'))



