"""Write a recursive function to reverse a string"""

input_text = input('Please, enter your text:\n')


def reversed_text(string):
    if len(string) == 1:
        return string
    else:
        return f'{string[-1]}{reversed_text(string[:-1])}'


print(reversed_text(input_text))
