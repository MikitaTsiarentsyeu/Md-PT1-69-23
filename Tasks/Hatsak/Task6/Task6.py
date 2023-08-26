def string_reverse(s: str) -> str:
    """1. Write a recursive function to reverse a string."""
    if s == '':
        return ''
    return s[-1] + string_reverse(s[:-1])


print(string_reverse('qwerty'))


def check_palindrome(s: str) -> str:
    """2. Write a recursive function to check whether a given string is a palindrome."""
    if s == '':
        return True
    if s[0] != s[-1]:
        return False
    return check_palindrome(s[1:-1])


print(check_palindrome('abcba'))
print(check_palindrome('abccba'))
print(check_palindrome('abcbaa'))


def count_chr(s: str, char: str) -> int:
    """3. Write a recursive function to count the number of occurrences of a given character in a string."""
    if char not in s:
        return 0
    return 1 + count_chr(s[s.find(char) + 1:], char)


test_string = 'abc abba count a number of chars'
check_char = 'a'

print(count_chr(test_string, check_char) == test_string.count(check_char))


def count_power(n: int, x: int) -> int:
    """4. Write a recursive function to calculate the power of a given number."""
    if x == 0:
        return 1
    return n*count_power(n, x-1)


print(count_power(10, 10))


def find_fibonacchi(n: int) -> int:
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    return find_fibonacchi(n-1) + find_fibonacchi(n-2)


print(find_fibonacchi(8))