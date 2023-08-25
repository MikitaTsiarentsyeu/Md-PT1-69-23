def file(a):
    try:
        f = open(a,'r')
        return print(f.read())
    except FileNotFoundError:
        print("File not found")
file(a ='TextFileFor2.txt')
file(a='ascsdsdc.txt')