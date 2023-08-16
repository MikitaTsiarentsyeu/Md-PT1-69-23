
def read_a_file():
    """
    a function that reads a file and returns its contents as a string
    """
    try:
        with open("Task7.txt", "r") as file:
            text = str(file.read())
            return print(text)
    except FileNotFoundError:
        return print("File not found")

                 
read_a_file()