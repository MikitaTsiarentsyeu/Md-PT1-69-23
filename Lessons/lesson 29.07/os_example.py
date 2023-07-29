import os

pathes = ["test leve 1", "test level 2", "test level 3"]

# print('\\'.join(pathes))

print(os.name)
sep = "\\" if os.name == "nt" else '/'

print(os.sep)
print(os.sep.join(pathes))

print(os.path.join(*pathes))

# os.makedirs(os.sep.join(pathes))

print(os.getcwd())

print(os.listdir())

for l in os.walk(os.getcwd()):
    print(l)

# os.chdir(os.sep.join(pathes))

# print(os.getcwd())

# open("test.txt", 'w')