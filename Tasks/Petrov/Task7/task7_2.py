def read_file(name: str) -> str:
    """Return the content of a file.

    name
        full name of a file.
    """
    try:
        with open(name, "r", encoding="UTF-8") as file:
            text = file.read()
            return text

    # If file with given name doesn't exist, FileNotFoundError raises
    except FileNotFoundError:
        return "File not found"


while True:
    print("Input full file name which you want to open", end="")
    print("or 1 to exit: ", end="")
    file_name = input()

    # Letting user read files until 1 is put as an input
    if file_name == "1":
        break
    else:
        print(read_file(file_name))
        print("Done")
