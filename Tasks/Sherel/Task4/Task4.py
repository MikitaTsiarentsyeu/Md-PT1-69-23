def input_validation(func):
    def wrapper():
        while True:
            try:
                user_input = int(
                    input("Enter maximum number of characters per line, an integer that must be greater than 35: "))
                if user_input <= 35:
                    print("Restart the program and enter a value greater than 35.")
                else:
                    return user_input
            except ValueError:
                print("Invalid input. Enter an integer.")
                continue

    return wrapper

@input_validation
def get_user_input():
    pass

def format_lines(lines, user_input):
    formatted_lines = []

    for line in lines:
        words = line.split()

        formatted_line = ""
        current_length = 0

        for word in words:
            word_length = len(word)
            if current_length + word_length <= user_input - 1:
                formatted_line += word + " "
                current_length += word_length + 1
            else:
                for str_length in formatted_line[:-1].split("\n"):
                    difference = user_input - len(str_length)
                    while difference != 0:
                        str_length = str_length.replace(" ", "  ", difference)
                        difference = user_input - len(str_length)
                    formatted_lines.append(str_length)
                    formatted_line = word + " "
                    current_length = word_length + 1
        formatted_lines.append(formatted_line.rstrip())

    return formatted_lines

def write_output_file(output_lines):
    with open("output_text.txt", "w") as output_file:
        for line in output_lines:
            output_file.write(line + "\n")

with open("text.txt", "r") as input_file:
    lines = input_file.readlines()

user_input = get_user_input()
formatted_lines = format_lines(lines, user_input)
write_output_file(formatted_lines)
