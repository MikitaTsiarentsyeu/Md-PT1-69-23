"""4. Write a function that takes a string as an argument and returns two numbers,
first for count of lower case symbols, second for count of the upper case symbols in the initial string."""

my_string = 'HellO WorlD!!!'


def count_case(string):
    l, u = 0, 0
    for s in string:
        if not s.isalpha():
            continue
        print(s)
        if s.islower():
            l += 1
            print('l: ', l)
        else:
            u += 1
            print('u: ', u)

    return l, u


print(count_case(my_string))