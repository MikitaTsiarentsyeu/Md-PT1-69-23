NUMBER_OF_SYMBOLS = 40

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

        if len(string) < 41:
            end_str = ''
        else:
            string, end_str = string.rsplit(maxsplit=1)

        spaces = NUMBER_OF_SYMBOLS - len(string)

        string = string.split()

        i = 0
        while i < spaces:
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
