"""Write a recursive function to check whether a given string is a palindrome"""

import string

input_text = input("Please, enter your text:\n")


def is_palindrome(text):
    for symbol in string.punctuation:
        if symbol in text:
            text = text.replace(symbol, '')

    text = text.lower()

    if len(text) <= 1:
        return print("Your text is a palindrome")
    elif text[0] == text[-1]:
        is_palindrome(text[1:-1])
    else:
        return print("Your text is not a palindrome")


is_palindrome(input_text)
