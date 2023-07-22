strings = input('Please, input a list of strings in format: "string--string--string":\n')
strings = strings.split('--')
count = []
for s in strings:
    if len(s) > 5:
        count.append(s)
if len(count) == 0:
    print('You did not input strings than length grater then 5 characters')
    exit()

print(f'Strings that have a length greater than 5 characters: {count}')



