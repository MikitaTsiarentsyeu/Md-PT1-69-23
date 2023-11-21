def your_palindrome(string):
    """2.The recursive function 
    to check whether a given 
    string is a palindrome"""
    if len(string) <= 1:
        return print("Your text is a palindrome")
    elif string[0] == string[-1]:
        your_palindrome(string[1:-1])
    else:
        return print("Your text is not a palindrome")
    
your_palindrome(input("Please, enter your string:\n"))