string = input("Please, input a string:\n")

string1 = ''
for s in range(len(string)):
    if string[s].isupper():
        elem = string[s].lower()
        string1 = string1 + elem

    else:
        elem = string[s].upper()
        string1 = string1 + elem

print(f'Your string where all capital letters converted to lowercase and vice versa: {string1}')

