"""task 7-2. Write a function that reads a file and returns its contents as a string.
Handle the FileNotFoundError and return "File not found" if the file does not exist."""

def read_file():
    try:
        with open("task 7-2.txt", "r") as file:
            return print(str(file.read()))

    except FileNotFoundError:
        print("File not found")


read_file()
