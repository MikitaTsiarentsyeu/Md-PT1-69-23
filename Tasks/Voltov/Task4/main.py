def input_validation(func):
    def wrapper():
        while True:
            try:
                user_input = int(input("Enter the maximum number of characters per line (more than 35): "))
                if user_input <= 35:
                    print("The value must be greater than 35. Try again.")
                else:
                    return user_input
            except ValueError:
                print("Invalid input. Enter an integer.")
                continue

    return wrapper

@input_validation
def get_user_input():
    pass

def crop_text(input_file, output_file, max_chars):
    cropped_lines = []

    with open(input_file, "r", encoding="windows-1251") as old_text:
        for line in old_text:
            while len(line) > max_chars:
                if line[max_chars-1] == ' ':
                    string_len = line[:max_chars].strip()
                    string_len_new = string_len.replace(' ', '  ', max_chars - len(string_len)-1)
                    cropped_lines.append(string_len_new + '\n')
                    line = line[max_chars:].lstrip()

                else:
                    string = line[0:max_chars].split()[:-1]
                    string_len = ' '.join(string)
                    space = max_chars - len(string_len)
                    num = 0
                    pos = 0
                    while num < space-1:
                        if pos == len(string) - 1:
                            pos = 0
                        string[pos] += ' '
                        num += 1
                        pos += 1
                    string_len_new = ' '.join(string)
                    cropped_lines.append(string_len_new + '\n')
                    line = line[len(string_len)+1:].lstrip()

                if len(line) <= max_chars:
                    cropped_lines.append(line)

    with open(output_file, 'w') as new_text:
        for line in cropped_lines:
            new_text.write(line)

    print(f"The edited text is saved in a file {output_file}")

if __name__ == "__main__":
    input_file = "text.txt"
    output_file = "cropped_text.txt"
    max_chars = get_user_input()
    crop_text(input_file, output_file, max_chars)