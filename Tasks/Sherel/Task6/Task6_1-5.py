"""1. Write a recursive function to reverse a string."""
def reverse_string(string):
    """
    :param string: a string
    :return: reverse a string
    """
    if len(string) <= 1:
        return string
    return reverse_string(string[1:]) + string[0]

input_str = input("Please, enter your string: ")
print(reverse_string(input_str))

# Input: "the test drive a recursive function"
# Output: "noitcnuf evisrucer a evird tset eht"