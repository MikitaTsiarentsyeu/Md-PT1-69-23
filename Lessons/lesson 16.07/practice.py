s = "hgfygtfytfuybvj iughiuhfinbk jbnio"

target = "u"

indexes = []

for i, symbol in enumerate(s):
    if symbol == target:
        indexes.append(i)
        # print(i)
        # break
# else:
#     print("symbol was not found")

if indexes:
    print(indexes)
else:
    print("symbol was not found")

count = {}
for i in s:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
print(count)

l = [3,6,4,2,4,67,98,65,3,34,67,4]

m = l[0]
for i in l:
    if i > m:
        m = i

print(m)