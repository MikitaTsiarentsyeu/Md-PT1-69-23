max_char = input('Please, enter the maximum number of characters per line (36 or more):\n')

while not max_char.isdigit() or int(max_char) <= 35:
    max_char = input('Wrong input. Please, enter an integer digit (36 or more):\n')

max_char = int(max_char)

with open('text.txt', 'r', encoding="utf-8") as text:
    parts = text.readlines()

new_text = []
count = 0
for line in parts:
    line = list(parts[count])
    while len(line) > max_char:
        if line[max_char] == ' ':
            line[max_char] = '\n'
            new_text.append(line[:max_char + 1])
            del line[:max_char + 1]
        else:
            line.insert(0, ' ')
    else:
        new_text.append(line[:])
        count += 1

for elem in new_text:
    index = 1
    while elem[0] == ' ' and index < len(elem):
        if elem[index] == ' ' and elem[index - 1] != ' ':
            elem.insert(index, ' ')
            del elem[0]
        elif index == (len(elem) - 1):
            index = 1
        else:
            index += 1

new_phrase = ""
num = 0
for elem in new_text:
    for e in elem:
        new_phrase += e
        num += 1

print(new_phrase)

with open('formatted_text.txt', 'w', encoding="utf-8") as new_file:
    new_file.write(new_phrase)
