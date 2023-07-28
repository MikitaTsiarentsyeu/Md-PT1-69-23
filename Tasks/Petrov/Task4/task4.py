class WrongNumberOfCharactersPerLine(Exception):
    pass


def make_lines(paragraph, needed_length):
    lines = []
    pos_start, pos_current = 0, 0
    while pos_current + needed_length < len(paragraph):
        pos_current += needed_length
        while paragraph[pos_current] != " ":
            pos_current -= 1
        line = paragraph[pos_start: pos_current].strip()
        index, round = 1, 1
        actual_length = len(line)
        while actual_length != needed_length:
            if line[index] == " ":
                line = f"{line[0:index+1]}{line[index:]}"
                index += round + 1
                actual_length = len(line)
            else:
                index += 1
            if index == actual_length:
                index = 1
                round += 1
        pos_start = pos_current
        lines.append(f"{line}\n")
    lines.append(paragraph if pos_current == 0 else paragraph[pos_current+1:])
    return lines


while True:
    try:
        length = int(input("Input maximum number of characters per line: "))
        if length <= 35:
            raise WrongNumberOfCharactersPerLine
        break
    except ValueError:
        print("Wrong input")
    except WrongNumberOfCharactersPerLine:
        print("Invalid value, must be greater than 35")

try:
    with open("text.txt", "r", encoding="utf-8") as file:
        output = open("output.txt", "w", encoding="utf-8")
        for section in file:
            section = make_lines(section, length)
            for line in section:
                output.write(line)
    output.close()
    print("Formatting completed, check output.txt for a formatted text.")
except FileNotFoundError:
    print("File does not exist")
