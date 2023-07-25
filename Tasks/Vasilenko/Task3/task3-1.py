"""Write a program that takes a string as input from a user
and returns the number of vowels in the string"""

print("Welcome to vowels calculator")

phrase = input("Please, enter a word or a phrase:\n")
phrase = phrase.lower()

all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
phrase_vowels = []

for vow in phrase:
    if vow in all_vowels:
        phrase_vowels.append(vow)
print(f'The number of vowels in your word or phrase: {len(phrase_vowels)}')
