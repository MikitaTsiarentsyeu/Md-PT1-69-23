sym = input('Please, input maximum number of characters per line, which must be greater than 35:\n')

if not sym.isdigit() or int(sym) <= 35:
    print('Your input is incorrect, try again')
    exit()
sym = int(sym)

cropped = []

with open('text.txt', 'r', encoding="windows-1251") as old_text:

    for line in old_text:
        while len(line) > sym:
            if line[sym-1] == ' ':
                string_len = line[:sym].strip()
                string_len_new = string_len.replace(' ', '  ', sym - len(string_len)-1)
                cropped.append(string_len_new + '\n')
                line = line[sym:].lstrip()

            else:
                string = line[0:sym].split()[:-1]
                string_len = ' '.join(string)
                space = sym - len(string_len)
                num = 0
                pos = 0
                while num < space-1:
                    if pos == len(string) - 1:
                        pos = 0
                    string[pos] += ' '
                    num += 1
                    pos += 1
                string_len_new = ' '.join(string)
                cropped.append(string_len_new + '\n')
                line = line[len(string_len)+1:].lstrip()

            if len(line) <= sym:
                cropped.append(line)

with open("cropped text.txt", 'w') as new_text:
    for element in cropped:
        new_text.write(element)

print('Cropped text you can find in the file "cropped text"')










