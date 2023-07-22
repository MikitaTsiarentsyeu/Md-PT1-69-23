string = input("Please, input the string\n")
symbol = ['.', ',', '-', "'", '"', ':', ';', '!', '?', '(', ')', '[', ']', '{', '}']
for log in symbol:
    if log in string:
        string = string.replace(log, '')

words = string.split()

count = {}
for n in words:
    if n not in count:
        count[n] = 1
    else:
        count[n] += 1
print(count)


