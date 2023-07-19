"""6. Write a program that takes a string as input and returns the string with all vowels removed."""

vowels = "eEyYuUiIoOaA"

user_input = input("Enter your string:\n")

for i in user_input:
    if i in vowels:
        user_input = user_input.replace(i, "")

print(user_input)