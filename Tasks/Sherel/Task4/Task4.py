""""
1. Prepare to read the contents of the file text.txt
2. Allow the user to enter a parameter "maximum number of characters per line", which must be greater than 35.
3. Format the text taking into account the maximum number of characters, but if a word does not fit entirely on a line, it should be moved to the next one, and the spacing between words should be evenly increased (similarly to the "Justify" function in text editors). There is a module called ‘textwrap’ which can do it, you may take a look at it but do not use for this task.
4. Write the resulting text to a new file and notify the user about it."""

user_input = int(input("Enter maximum number of characters per line, an integer that must be greater than 35: "))
if user_input < 35:
    print("Restart the program and enter a value greater than 35.")
    exit()

with open("text.txt", "r") as input_file:
    lines = input_file.readlines()

with open("output_text.txt", "w") as output_file:
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
                        difference = user_input-len(str_length)
                    output_file.write(str_length + "\n")
                    formatted_line = word + " "
                    current_length = word_length + 1
        output_file.write(formatted_line.rstrip() + "\n")