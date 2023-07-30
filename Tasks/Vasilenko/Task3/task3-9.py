"""Write a program that takes a string as input and returns the string reversed"""

print("Here you can reverse your text")

phrase = input("Please, enter your text:\n")

phrase_list = []

for e in phrase:
    phrase_list += e

phrase_list = phrase_list[::-1]

new_phrase = ""

for e in phrase_list:
    new_phrase += e

print(f'Your reversed text is: {new_phrase}')
