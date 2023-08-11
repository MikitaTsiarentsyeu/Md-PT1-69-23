def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

sent = str(input("Введите строку:\n"))

if (is_palindrome(sent) == True):
    print("Эта строка является палиндромом")
else:
    print("Эта строка не является палиндромом!")