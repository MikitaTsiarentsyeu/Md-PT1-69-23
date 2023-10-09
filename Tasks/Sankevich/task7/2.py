def open_file(file_name):
    try:
        f = open(file_name, mode='r')
        print(f.read())
        f.close()
        return 'File closed'
    except FileNotFoundError:
        return 'File not found'
    

print(open_file('rap.txt'))




