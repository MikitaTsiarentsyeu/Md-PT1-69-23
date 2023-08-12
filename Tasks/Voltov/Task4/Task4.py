# 1. Prepare to read the contents of the file text.txt
# 2. Allow the user to enter a parameter "maximum number of characters per line", which must be greater than 35.
# 3. Format the text taking into account the maximum number of characters, but if a word does not fit entirely on a line, it should be moved to the next one, and the spacing between words should be evenly increased (similarly to the "Justify" function in text editors). There is a module called ‘textwrap’ which can do it, you may take a look at it but do not use for this task.
# 4. Write the resulting text to a new file and notify the user about it.

with open("text.txt", "r") as input_file:
    text = input_file.read()

    max_chars = int(input("Enter the maximum number of characters per line (greater than 35): "))

    if max_chars <= 35:
        print("Error: value must be greater than 35")
    else:

        words = text.split()

        formatted_text = ""
        current_line = ""
        for word in words:
            if len(current_line + word) + 1 <= max_chars:
                current_line += word + " "
            else:
                words_in_line = current_line.strip().split()
                num_spaces = max_chars - sum(len(word) for word in words_in_line)
                num_gaps = len(words_in_line) - 1
                if num_gaps > 0:
                    spaces_per_gap = num_spaces // num_gaps
                    extra_spaces = num_spaces % num_gaps
                else:
                    spaces_per_gap = 0
                    extra_spaces = num_spaces
                formatted_line = ""
                for i, word in enumerate(words_in_line):
                    formatted_line += word
                    if i < len(words_in_line) - 1:
                        formatted_line += " " * (spaces_per_gap + 1)
                        if extra_spaces > 0:
                            formatted_line += " "
                            extra_spaces -= 1
                formatted_text += formatted_line.ljust(max_chars) + "\n"
                current_line = word + " "

        words_in_line = current_line.strip().split()
        formatted_line = " ".join(words_in_line)
        formatted_text += formatted_line.ljust(max_chars) + "\n"

        with open("format_text.txt", "w") as output_file:
            output_file.write(formatted_text)

        print("Text successfully formatted and written to file format_text.txt")