"""1. Write a recursive function to reverse a string."""
def reverse_string(string):
    """
    :param string: a string
    :return: reverse a string
    """
    if len(string) <= 1:
        return string
    return reverse_string(string[1:]) + string[0]

# input_str = input("Please, enter your string: ")
# print(reverse_string(input_str))

# Input: "the test drive a recursive function"
# Output: "noitcnuf evisrucer a evird tset eht"


"""2. Write a recursive function to check whether a given string is a palindrome."""
def check_str_palindrome(string):
    """
    :param string: a string
    :return: returns the answer whether the string is a palindrome or not
    """
    if len(string) <= 1:
        return string
    if len(string) % 2 == 0:
        check_midle = len(string) // 2
        string = string[:check_midle] + " " + input_str[check_midle:].lower()
    if string[0] == string[-1]:
        return check_str_palindrome(string[1:-1])
    return False

input_str = input("Please enter your string for check a given string is a palindrome: ")

if check_str_palindrome(input_str.lower().replace(" ", '')):
    print("Yes, this string is a palindrome")
else:
    print("I'm sorry, but this string dont is a palindrome")
