
def is_palindrome(string, start, end):
    """
    a recursive function to check whether
    a given string is a palindrome
    """
    string = string.lower()
    
    if start >= end:
        return True
    if string[start] != string[end]:      
        return False
    return is_palindrome(string, start+1, end-1)