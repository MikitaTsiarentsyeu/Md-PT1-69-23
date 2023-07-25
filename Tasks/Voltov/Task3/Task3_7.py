# 7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.


user_input = input("Enter the string: ")
result = ""
for letter in user_input:
    if letter.isalpha():
        if letter.islower():
            result += letter.upper()
        else:
            result += letter.lower()
    else:
        result += letter

print("Result:", result)