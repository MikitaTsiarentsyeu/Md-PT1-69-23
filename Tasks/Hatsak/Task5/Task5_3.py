"""3. Write a function that takes a list of strings as an argument
 and returns a new list with all the strings that have a length greater than 5."""

my_list = ['', ' ', 'a', 'ab', '12345', 'qwerty', 'ss ccc']


def check(strings, n=5):
    return [string for string in strings if len(string) > 5]


print(check(my_list))
