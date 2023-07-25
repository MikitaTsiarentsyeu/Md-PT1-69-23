from string import punctuation


string = [i.strip(punctuation) for i in input("Enter your string: ").split()]
words_dict = {}
for word in string:
    if not word:
        continue
    word = word.lower()
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
print("In your string there are such words:")
one, many = "time", "times"
for key, value in words_dict.items():
    print(f"{key}: {value} {one if value == 1 else many}")
