string = input('Please, input string to count the number of occurrences of a given character in a string:\n')
ch = input('Please, input the character:\n')


def count_char(string, ch):
    count = 0
    if string.find(ch) != -1:
        count = 1 + count_char(string[string.find(ch) + 1:], ch)
    return count


print(f'The number of occurrences of a character in a string is: {count_char(string, ch)}')
