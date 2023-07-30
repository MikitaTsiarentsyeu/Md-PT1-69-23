def search_count(text, search):
    if len(text) == 1:
        return 1 if text in search else 0
    else:
        return search_count(text[-1], search) + search_count(text[:-1], search)


string = input("Input a string: ")
vowels = "eyuioa"
count = search_count(string.lower(), vowels) if string else 0
print(f"Number of vowels in your string is {count}")
