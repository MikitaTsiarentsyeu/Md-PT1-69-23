list = list(map(str,input("Input your words using comma:\n").split(",")))
dict = {}

for i in list:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(f"Dictionary with the count of each word in the string:\n{dict}")

