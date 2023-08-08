from string import punctuation


def ispalindrome(text):
    if len(text) <= 1:
        return True
    else:
        if text[0] == text[-1]:
            return ispalindrome(text[1:-1])
        return False


line = input("Input text: ")
if line:
    without_all = str.maketrans("", "", punctuation + " ")
    flag_without_all = ispalindrome(line.lower().translate(without_all))
    with_spaces = str.maketrans("", "", punctuation)
    flag_with_spaces = ispalindrome(line.lower().translate(with_spaces))
    print(f"Is your input a palindrome? {flag_without_all}")
    print(f"Is your input a palindrome with spaces? {flag_with_spaces}")
else:
    print("There is no input")
