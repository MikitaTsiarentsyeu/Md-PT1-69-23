class WrongNumberOfCharactersPerLine(Exception):
    pass


def make_lines(paragraph, line_length):
    lines = []
    position_start, position_current = 0, 0
    while position_current + line_length < len(paragraph):
        position_current += line_length
        while paragraph[position_current] != " ":
            position_current -= 1
        line = paragraph[position_start: position_current].strip()
        index, round = 1, 1
        while True:
            if line[index] == " ":
                line = f"{line[0:index+1]}{line[index:]}"
                index += round + 1
            else:
                index += round
            if len(line) == line_length:
                break
            if index >= len(line):
                index = 0
                round += 1
        position_start = position_current
        lines.append(f"{line}\n")
    lines.append(paragraph[position_current+1:])
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
