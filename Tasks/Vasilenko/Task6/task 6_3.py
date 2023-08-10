"""Write a recursive function to count the number of occurrences of a given character in a string"""

input_text = input("Please, enter your text:\n")
input_symbol = input('Please, enter a symbol you want to count:\n')


def symbol_count(text, symbol, count=0):

    if len(text) == 1:
        if symbol == text[0]:
            return count + 1
        else:
            return count
    else:
        if symbol == text[0]:
            return symbol_count(text[1:], symbol, count + 1)
        else:
            return symbol_count(text[1:], symbol, count)


print(f'The number of your symbol in your text is {symbol_count(input_text, input_symbol)}')
