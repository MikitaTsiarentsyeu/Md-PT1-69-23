dictSzerel = {
    "work1": "1. Write a recursive function to reverse a string.",
    "work2": "2. Write a recursive function to check whether a given string is a palindrome.",
    "work3": "3. Write a recursive function to count the number of occurrences of a given character in a string.",
    "work4": "4. Write a recursive function to calculate the power of a given number.",
    "work5": "5. Write a recursive function to find the Nth number in the Fibonacci sequence. "
             "0, 1, 2, 3, 5, 8, 13, 21, ...",
}

def reverse_string(string):
    """
    a recursive function
    :param string: a string
    :return: reverse a string
    """
    if len(string) <= 1:
        return string
    return reverse_string(string[1:]) + string[0]

input_str = input("{}\nPlease, enter your string: ".format(dictSzerel["work1"]))
print(reverse_string(input_str))
# Input: "the test drive a recursive function"
# Output: "noitcnuf evisrucer a evird tset eht"


def check_str_palindrome(string):
    """
    a recursive function
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

input_str = input("{}\nPlease, enter your string: ".format(dictSzerel["work2"]))
rep = ",.:;!?-#@$%^&*()_+|/'’"
input_str = ''.join([x for x in input_str if x not in rep])

if check_str_palindrome(input_str.lower().replace(" ", '')):
    print("Yes, this string is a palindrome")
else:
    print("I'm sorry, but this string don't is a palindrome")
# Input 1: "Go Hang a salami I'm a lasagna hog"
# Output 1: "Yes, this string is a palindrome"

# Input 2: "Hi bro"
# Output 2: "I'm sorry, but this string don't is a palindrome"


def count_occurrences(user_string, user_char):
    """
    a recursive function
    :param user_string: a string
    :param user_char: a given character
    :return: number of occurrences of a given character in a string
    """
    if len(user_string) == 0:
        return 0
    elif user_string[0] == user_char:
        return 1 + count_occurrences(user_string[1:], user_char)
    else:
        return count_occurrences(user_string[1:], user_char)

user_string = input("{}\nPlease, enter your string: ".format(dictSzerel["work3"]))
user_char = input("Please enter your char: ")

print("Result: ", count_occurrences(user_string, user_char))
# Input 1: You can cage a swallow, can’t you, but you can’t swallow a cage, can you?
# Input 2: y
# Output: 3


def calculate_power(number, degree):
    """
    a recursive function, without validation
    :param number: integer or float number
    :param degree: integer or float degree
    :return: the given number to the desired power
    """
    if degree == 0:
        return 1
    if degree < 0:
        return calculate_power(number, degree+1)/number
    if degree > 0:
        return number * calculate_power(number, degree-1)

input_number = input("{}\nPlease, enter your number: ".format(dictSzerel["work4"]))
input_degree = input("Ok, enter degree: ")

print("Result: ", calculate_power(float(input_number), float(input_degree)))
# Input 1: 2
# Input 2: -5
# Output: 0.03125


def fibonacci_positive(user_input):
    """
    fibonacci function for positive values
    :param user_input: integer value
    :return: find the Nth number in the Fibonacci sequence
    """
    if user_input == 0:
        return 0
    if user_input in (1, 2):
        return 1
    return fibonacci_positive(user_input - 1) + fibonacci_positive(user_input - 2)

def fibonacci_negative(user_input):
    """
    fibonacci function for negative values
    :param user_input: integer value
    :return: find the Nth number in the Fibonacci sequence
    """
    return fibonacci_positive(user_input) * (-1)**(user_input+1)

def fibonacci_input_validation():
    """
    user-entered data validation function
    :return: the result of a positive or negative function, depending on the conditions
    """
    try:
        user_input = int(input("{}\nEnter integer: ".format(dictSzerel["work5"])))
        if user_input == 0:
            return print(fibonacci_positive(user_input))
        elif user_input >= 1:
            return print(fibonacci_positive(user_input-1))
        elif user_input < 0:
            return print(fibonacci_negative((user_input+1)*(-1)))
        else:
            return user_input
    except ValueError:
        print("Invalid input. Enter an integer.")

fibonacci_input_validation()
# Input 1: 8
# Output 1: 13

# Input 2: -10
# Output 2: 34