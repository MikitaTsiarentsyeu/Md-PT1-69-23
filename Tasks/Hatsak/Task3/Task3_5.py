"""5. Write a program that takes a list of strings as input and
returns a list with all strings that have a length greater than 5 characters."""
strings = ['12', '00000', 'Hello! My friend!', 'How are you?', '\n\r\d\\\\', 'LOVE', '']
n = 5


def pick(arr, k):
    return [s for s in arr if len(s)>k]


print(pick(strings, n))
