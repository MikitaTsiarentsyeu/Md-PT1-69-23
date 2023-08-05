"""2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed."""

my_list = ['', ' ', 'a', 'ab', '12345', 'qwerty', 'ss ccc']


def rev(strings):
    return [string[::-1] for string in strings]


print(rev(my_list))