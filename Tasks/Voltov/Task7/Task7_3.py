# Write a function that takes a list of
# integers as input and returns the sum of
# all even numbers in the list. Handle the TypeError
# and return "Invalid input type" if the input
# is not a list or not every element is int.

def sum_even_numbers(lst):
    if type(lst) != list or not all(isinstance(x, int) for x in lst):
        return "Invalid input type"
    return sum(filter(lambda x: x % 2 == 0, lst))
