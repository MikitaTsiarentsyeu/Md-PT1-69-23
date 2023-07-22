# 6. Write a program that takes a string as input and returns the string with all vowels removed.


user_input = input("Enter the string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
result = ""
for letter in user_input:
    if letter.lower() not in vowels:
        result += letter

print("String without vowels:", result)

# version for Russian
def remove_vowels(string):
    vowels = "аеёиоуыэюя"
    new_string = ""
    for letter in string:
        if letter.lower() not in vowels:
            new_string += letter
    return new_string

string = input("Введите строку: ")

print("Строка без гласных букв:", remove_vowels(string))