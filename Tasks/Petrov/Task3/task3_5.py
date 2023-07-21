text = []
print("Input your string. Print \"exit\" to stop inputting strings")
while True:
    line = input()
    if line == "exit":
        break
    text.append(line)

i = 0
size = len(text)
while i < size:
    if len(text[i]) <= 5:
        del text[i]
        i -= 1
        size -= 1
    i += 1

if text:
    print("Strings that have a length greater than 5 characters are:")
    for line in text:
        print(line)
else:
    print("No strings that have a length greater than 5 characters :(")
