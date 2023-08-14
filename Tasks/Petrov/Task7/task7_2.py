
def read_file(name):
    with open(name, "r", encoding="UTF-8") as file:
        return file.read()


while True:
    try:
        print("Input full file name which you want to open", end="")
        print("or 1 to exit: ", end="")
        file_name = input()

        if file_name == "1":
            break
        else:
            output = read_file(file_name)
            print(output)
            print("Done")
    except FileNotFoundError:
        print("File not found")
