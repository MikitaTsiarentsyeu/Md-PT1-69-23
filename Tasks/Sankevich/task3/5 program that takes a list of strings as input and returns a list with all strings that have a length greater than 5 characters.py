list_of_strings = []

while True:
    string = input('print something or end by printing "done" ')
    if string == "done":
        break

    if len(string) < 5:
        print("Print longer string")
        continue
    else:
        list_of_strings.append(string)

print("Here's your strings longer than 5: ", list_of_strings) 