string = input('Please, input a string:\n')
string1 = ''

for s in range(-1, -len(string)-1, -1):
    string1 = string1 + string[s]

print(f'Your string reversed is: {string1}')

