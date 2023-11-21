def number_of_occurrences(string, simb):
    """3.The recursive function - 
    counter the number of occurrences 
    of a given character in a string"""
    if len(string)==0:
        return 0
    elif string[0]==simb:
        return number_of_occurrences(string[1:], simb)+1
    else:
        return number_of_occurrences(string[1:], simb)
n=number_of_occurrences(input("Please, enter your string:\n"), input("Please, enter your simbol:\n"))
print(f"Your simbol was found {n} time(s) in the string.") 