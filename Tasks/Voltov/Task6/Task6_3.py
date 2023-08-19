# 3. Write a recursive function to count the number of occurrences of a given character in a string.

def count_char(s, c):
    if len(s) == 0:
        return 0
    elif s[0] == c:
        return 1 + count_char(s[1:], c)
    else:
        return count_char(s[1:], c)

print(count_char("hello", "l"))

