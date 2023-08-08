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

# input_str = input("Please enter your string: ")
# rep = ",.:;!?-#@$%^&*()_+|/'’"
# input_str = ''.join([x for x in input_str if x not in rep])
#
# if check_str_palindrome(input_str.lower().replace(" ", '')):
#     print("Yes, this string is a palindrome")
# else:
#     print("I'm sorry, but this string dont is a palindrome")

"""3. Write a recursive function to count the number of occurrences of a given character in a string."""
def count_occurrences(user_string, user_char):
    if len(user_string) == 0:
        return 0
    elif user_string[0] == user_char:
        return 1 + count_occurrences(user_string[1:], user_char)
    else:
        return count_occurrences(user_string[1:], user_char)

# user_string = input("Please enter your string: ")
# user_char = input("Please enter your char: ")
#
# print(count_occurrences(user_string, user_char))
# Input 1: You can cage a swallow, can’t you, but you can’t swallow a cage, can you?
# Input 2: y
# Output: 3

"""4. Write a recursive function to calculate the power of a given number."""
