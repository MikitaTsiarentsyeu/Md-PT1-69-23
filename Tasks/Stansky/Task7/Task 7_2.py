def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text_string = file.read()
            # print(type(text_string))
            return text_string
    except FileNotFoundError:
        return "File not found"


print(read_file("text5577.txt"))
print(read_file("text.txt"))

