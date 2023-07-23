# f = open("test.txt", "r")
# print(f.read())
# f.close()

# with open(r"C:\Drive D\Projects\IT Academy\Python\Md-PT1-69-23\Md-PT1-69-23\Lessons\lesson 23.07\test.txt", "r") as f:
#     print(f.read())

with open("test.txt", 'w') as f:
    f.write("test content\n")
    f.write("another test content\n")
    f.writelines(["line 1\n", "line 2\n", "line 3\n"])

with open("test.txt", 'r') as f:
    for symbol in f.read():
        print(repr(symbol))
    # for line in f:
    #     print(repr(line))
    # print(f.readlines())
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(10))
    # print(f.read(100))
    # print(f.read())
    # f.seek(0)
    # print(f.read())
    # f.seek(0)
    # print(f.read())


with open("test.txt", 'a') as f:
    f.write("new content from append\n")

with open("test.txt", 'a+') as f:
    f.seek(0)
    print(repr(f.read()))
    f.seek(0)
    f.write("new content from append\n")
    print(repr(f.read()))

with open("test.txt", 'r+') as f:
    print(repr(f.read()))
    f.seek(0)
    f.write("content from r+ mode    ")
    print(repr(f.read()))
    f.write("the end")