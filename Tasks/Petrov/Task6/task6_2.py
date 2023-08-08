from string import punctuation


def ispalindrome(text):
    if len(text) <= 1:
        return True
    else:
        if text[0] == text[-1]:
            return ispalindrome(text[1:-1])
        return False


line = input("Input text: ").lower()
if line:
    line = line.translate(str.maketrans("", "", punctuation))
    flag_with_spaces = ispalindrome(line)
    line = line.translate(str.maketrans("", "", " "))
    flag_without_all = ispalindrome(line) if line else False
    print("Is your input a palindrome? ", end="")
    if flag_with_spaces and flag_without_all:
        print("Yes")
    elif flag_without_all:
        print("Only without spaces in count")
    elif flag_with_spaces:
        print("Only with spaces in count")
    else:
        print("No")
else:
    print("There is no input")
