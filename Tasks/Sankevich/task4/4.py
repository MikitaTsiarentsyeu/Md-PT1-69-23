copy_file = open("myfile.txt", "a")

string_length = 40
string_start = 0

space_position = 0

line_space_pos = 0
space_helper = 0

with open("text.txt", "r") as file:
    for line in file:
        if len(line) <= 40:
            string_from_file = line
            copy_file.write(string_from_file + '\n')
            
        else:
            while len(line) > 40:

                string_from_file = line[:string_length + 2]
                string_from_file = string_from_file.strip()
                space_position = string_from_file.rfind(' ')
                string_from_file = string_from_file[:space_position]

                while len(string_from_file) < 40:
                    line_space_pos = string_from_file.find(' ', line_space_pos + 2)
                    if line_space_pos == -1:
                        line_space_pos = 0
                    string_from_file = string_from_file[:line_space_pos] + ' ' + string_from_file[line_space_pos:]
                    space_helper += 1
                    string_from_file = string_from_file.strip()
                line_space_pos = 0
                space_helper = 0

                copy_file.write(string_from_file + '\n')

                string_start = space_position + 1

                line = line[string_start:]
        copy_file.write(line)

    line = line.strip()



file.close()


#   вЂ™
