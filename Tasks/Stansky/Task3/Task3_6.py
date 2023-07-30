string = input('Please, enter a string:\n')
vow = ['a', 'e', 'o', 'i', 'u', 'y', 'A', 'E', 'O', 'I', 'U', 'Y']
for v in vow:
    if v in string:
        string = string.replace(v, '')
print(f'Your string without vowels is: {string}')