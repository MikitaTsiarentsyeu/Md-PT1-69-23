"""Write a program that takes a string as input and returns the string with all vowels removed"""

print("Here you can remove all of the vowels from your text")

phrase = input("Please, enter a word or a phrase:\n")
phrase = phrase.lower()

all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']

for vow in phrase:
    if vow in all_vowels:
        phrase = phrase.replace(vow, '')

print(f'Your text without vowels: {phrase}')
