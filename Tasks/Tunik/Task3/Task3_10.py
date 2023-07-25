list = list(map(int,input("Enter the numbers using comma:\n").split(",")))

a = 2
newlist = []

for i in list:
    if i == 1:
        newlist.append(i)
        list.remove(i)

for i in list:
    if i == 2:
        newlist.append(i)
        list.remove(i)

for i in list:    
    while i % a != 0:
        a += 1
        if i == a:
            newlist.append(i)
    else:   
        a = 2

biggest = 0
for i in newlist:
    if i > biggest:
        biggest = i
print(f"The largest prime number in the list - {biggest}")

