
def read_file(name):
    try:
        with open(name, "r", encoding="UTF-8") as file:
            text = file.read()
            return text
    except FileNotFoundError:
        return "File not found"


while True:
    print("Input full file name which you want to open", end="")
    print("or 1 to exit: ", end="")
    file_name = input()

    if file_name == "1":
        break
    else:
        print(read_file(file_name))
        print("Done")
