"""1. Write a program that takes a string as input from a user and returns the number of vowels in the string."""

vowels = "eyuioa"
values = []

text = input("Enter your string:\n")
my_text = list(text.lower())
my_text.sort()

for i in my_text:
    if i in vowels:
        values.append(i)

print("The number of vowels in the string:", len(values))
