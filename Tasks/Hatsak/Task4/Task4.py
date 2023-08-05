NUMBER_OF_SYMBOLS = 40


def enter():
    NUMBER_OF_SYMBOLS = input("Enter the number >= 15 of symbols in a row: ")
    if not NUMBER_OF_SYMBOLS.isdigit() or int(NUMBER_OF_SYMBOLS) < 15:
        return enter()
    return int(NUMBER_OF_SYMBOLS)


NUMBER_OF_SYMBOLS = enter()
write_file = open('answer.txt', 'w')

with open("text.txt", "a+") as f:
    f.seek(0)
    end_str = ''
    string = 'T'
    while string:

        string = end_str + f.read(NUMBER_OF_SYMBOLS + 1 - len(end_str))

        if string == '':
            continue

        if '\n' in string:
            string, _, end_str = string.partition('\n')
            write_file.write(string + '\n')
            print(string)
            continue

        if string[-1] == ' ':
            end_str = ''
            write_file.write(string + '\n')
            print(string)
            continue

        if len(string) < NUMBER_OF_SYMBOLS + 1:
            end_str = ''
        else:
            string, end_str = string.rsplit(maxsplit=1)

        spaces = NUMBER_OF_SYMBOLS - len(string)

        string = string.split()

        i = 0
        while string[0:-1] and i < spaces:

            for j, word in enumerate(string[0:-1]):
                word = word + ' '
                string[j] = word
                i += 1
                if i >= spaces:
                    break

        string = ' '.join(string)
        write_file.write(string + '\n')
        print(string)
write_file.close()
