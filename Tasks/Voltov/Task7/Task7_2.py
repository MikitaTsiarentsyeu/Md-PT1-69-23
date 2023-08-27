# Write a function that reads a file and
# returns its contents as a string. Handle
# the FileNotFoundError and return "File not
# found" if the file does not exist.

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"