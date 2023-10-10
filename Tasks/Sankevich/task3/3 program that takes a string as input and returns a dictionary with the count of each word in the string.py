string = input()
some_list = []

words = string.lower().split()

for i in range(len(words)):
    s = words[i]
    if ',' in s:
        new_s = s.replace(',', '')
        s = new_s
    elif '.' in s:
        new_s = s.replace('.', '')
        s = new_s
    elif '!' in s:
        new_s = s.replace('!', '')
        s = new_s
    elif '?' in s:
        new_s = s.replace('?', '')
        s = new_s

    some_list.append(s)

uniq_list = []

for i in range(len(some_list)):
    if some_list[i] not in uniq_list:
        uniq_list.append(some_list[i])


for i in range(len(uniq_list)):
    print('Number of', '"', uniq_list[i], '"', 'is', some_list.count(uniq_list[i]))