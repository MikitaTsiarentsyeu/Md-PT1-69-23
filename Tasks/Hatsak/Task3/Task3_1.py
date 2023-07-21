"""1. Write a program that takes a string as input from a user and returns the number of vowels in the string."""
my_string = 'I love you'
#my_string = input('Enter any string: ')
vowels = 'ouieay'
counter = 0
for i in my_string:
    if i.lower() in vowels:
        counter += 1
print(counter)