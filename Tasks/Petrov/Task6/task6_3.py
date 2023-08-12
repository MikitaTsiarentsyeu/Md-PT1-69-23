def search_count(text, search):
    if len(text) == 1:
        return 1 if text in search else 0
    else:
        return search_count(text[-1], search) + search_count(text[:-1], search)


string = input("Input a string: ")
while True:
    seek = input("Input a character to search for: ")
    if len(seek) != 1:
        print("You need to input a single character")
        continue
    break
count = search_count(string.lower(), seek) if string else 0
print(f"Number of \"{seek}\" in your string \"{string}\" is {count}.")
