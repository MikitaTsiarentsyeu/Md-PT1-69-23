"""Write a program that takes a string as input
and returns the string with all capital letters converted to lowercase and vice versa"""

print("Here you can convert uppercase to lowercase and vice versa")

phrase = input("Please, enter a word or a phrase:\n")

phrase_list = []

for e in phrase:
    if e.islower():
        phrase_list += e.upper()
    elif e.isupper():
        phrase_list += e.lower()
    else:
        phrase_list += e

new_phrase = ""

for e in phrase_list:
    new_phrase += e

print(f'Your text with converted elements: {new_phrase}')
