"""1. Write a program that takes a string as input from a user and returns the number of vowels in the string."""

vowels = "eyuioa"
values = []

user_input = input("Enter your string:\n")
f_user_input = list(user_input.lower())
f_user_input.sort()

for i in f_user_input:
    if i in vowels:
        values.append(i)

print("The number of vowels in the string:", len(values))