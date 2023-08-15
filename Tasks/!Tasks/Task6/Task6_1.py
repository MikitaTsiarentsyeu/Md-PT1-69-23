
def reverse_string(string):
    """ a recursive function to reverse a string """
    
    if len(string) <= 1:
        return string
    return reverse_string(string[1:]) + string[0]