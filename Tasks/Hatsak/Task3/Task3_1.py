my_string = 'I love you'
vowels = 'ouieay'
counter = 0
for i in my_string:
    if i.lower() in vowels:
        counter += 1
print(counter)