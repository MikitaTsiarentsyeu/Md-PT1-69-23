list = list(map(str,input("Input your words using comma:\n").split(",")))

final = []

for i in list:
    if i not in final and len(i)> 5:
        final.append(i)
print(f"List with all strings that have a length greater than 5 characters:\n{final}")