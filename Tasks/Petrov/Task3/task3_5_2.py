text = []
print("Input your string. Print \"exit\" to stop inputting strings")
while True:
    line = input()
    if line == "exit":
        break
    text.append(line)

text2 = []
for string in text:
    if len(string) > 5:
        text2.append(string)

if text2:
    print("Strings that have a length greater than 5 characters are:")
    for line in text2:
        print(line)
else:
    print("No strings that have a length greater than 5 characters :(")
