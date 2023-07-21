str = input("Please input your string whithout any punctuation mark and special symbols, you can use only space:\n")

list = []

for i in str:
    if i == i.lower():
        list.append(i.upper())
    else:
        list.append(i.lower())
print(f'The string with all capital letters converted to lowercase and vice versa:\n{"".join(list)}')

