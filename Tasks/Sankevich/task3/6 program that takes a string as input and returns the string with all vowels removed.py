string = input("Just type some string: ")
just_list = []

for i in range(len(string)):
    if string[i] in 'aeouyiAEOIYU':
        continue
    else:
        just_list.append(string[i])

no_vowels_string = ''.join(just_list)

print("here is no vowels string", no_vowels_string)
