vow = ['a', 'e', 'o', 'i', 'u', 'y']
string = input("Please, input a string in English and you will get number оf vowels:\n")
string = string.lower()
vowels = []

for s in string:
    if s in vow:
        vowels.append(s)

if len(vowels) == 0:
    print('This string has no vowels!')
    exit()

print(f'Vowels: {vowels}, number of vowels is: {len(vowels)}')

