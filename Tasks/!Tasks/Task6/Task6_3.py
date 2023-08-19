def count_occur(string, char):
    """
    a recursive function to count the number of
    occurrences of a given character in a string
    """
    
    if len(string) == 0:
        return 0
    elif string[0] == char:
        return 1 + count_occur(string[1:], char)
    else:
        return count_occur(string[1:], char)

string = input("Please, input a string: ")
char = input("Please, input a char: ")

print(f"Char '{char}' was found {count_occur(string, char)} \
time(s) in the string.")