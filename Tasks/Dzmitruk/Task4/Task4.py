text_width = int(input("Please, input maximum number of characters per \
line, which must be greater than 35: "))

while text_width <= 35:
    text_width = int(input("Oops, something wrong, try again: "))

with open ("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

with open ("new_text.txt", "w", encoding="utf-8") as output_file:

    words = text.split()
    line = ""
    lines = []

    for word in words:
        if len(line) + len(word) + 1 <= text_width:
            line += word + " "
        else:
            lines.append(line.rstrip())
            line = word + " "
    lines.append(line)

    for new_string in lines:
        dif = text_width - len(new_string)
        while dif != 0:
            new_string = new_string.replace(" ", "  ", dif)
            dif = text_width - len(new_string)
              
        output_file.write(new_string + "\n")
    print("Formatting completed, check new_text.txt to see a formatted text.")