import string
s = input("Enter string to check for palindrome :\n")
for element in string.punctuation:
    if element in s:
        s = s.replace(element, '')
s = s.strip()
s = s.lower()


def palindrome_check(s):
    if len(s) < 2:
        return "The string is a palindrome"
    else:
        if s[0] == s[-1]:
            return palindrome_check(s[1:-1])
        else:
            return "The string is not palindrome"


print(palindrome_check(s))