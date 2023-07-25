list = list(map(int,input("Enter the numbers using comma:\n").split(",")))

m = 0
for i in list:
    if i > m:
        m = i
list.remove(m)
m = 0
for i in list:
    if i > m:
         m = i
print(f"The second largest number in the list - {m}")

