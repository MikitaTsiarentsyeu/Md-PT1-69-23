from string import punctuation

string = input("Input a string: ")
new_string = ""
for char in string:
    if char in punctuation or char == " " or char.isdigit():
        new_string = f"{new_string}{char}"
    elif char.islower():
        new_string = f"{new_string}{char.upper()}"
    elif char.isupper():
        new_string = f"{new_string}{char.lower()}"
print(new_string)
