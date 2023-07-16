l = [1,2,3,4,5,6,7,8,9]

# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5])

i = 0

while i<len(l):
    print(l[i])
    i+=1
# else:
#     print("the end")

for elem in l:
    print(elem)

print(elem)

flag = True
for symbol in "test str":
    if flag:
        print(symbol.upper())
    else:
        print(symbol.lower())
    flag = not flag


for s in "t e s t s t r     ":
    if s == " ":
        continue
    print(s)

count = -1

stop = False
while count < 10:
    count += 1
    if count > 5:
        stop = True
        break
    if count % 2 == 0:
        continue
    print(count)
else:
    print("the end")

if not stop:
    print("the end")

l = [1,2,3,4,5]

i = 0
while True:
    if i == len(l):
        break
    print(l[i])
    i += 1

for i in set("test str"):
    print(i)

for i in (1,2,3,4,5):
    print(i)

d = {1:"one", 2:"two", 3:"three"}

for key in d:
    print(key, d[key])

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

l = [[1,2,3], (4,5,6), {7,8,9}]
for i in l:
    for j in i:
        print(j)

# l = [1]
# for i in l:
#     l.append(i)
#     print(l)

for i in range(1,10,2):
    print(i)

print(list(range(100)))

s = "test str"
for i in range(len(s)-1):
    print(s[i]+s[i+1])

for i, e in enumerate(s):
    print(i, e)

for number, digit in zip([1,2,3,4], "123"):
    print(number, repr(digit))
