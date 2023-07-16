d = {1:"one", 2:"two", 3:"three"}

d = {"one":1, "two":2, "three":3}

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

# print(d["five"]) KeyError

print("five" in d)
print("three" in d)

print(2 in d.values())
print(4 in d.values())

print(d.get("five"))
print(d.get("three"))
print(d.get("five", "haven't found anything"))
print(d.get("three", "haven't found anything"))

d = dict([('one', 1), ("two", 2), ('three', 3)])
print(d)

one = "test"

print(dict(one=1, two=2, three=3))

print(one)

l = [[1,2,3], [4,5,6], [7,8,9]]
print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

print(len(l))

# l = []
# l.append(l)
# print(l)
# print(l[0][0][0][0][0][0])
# print(len(l))

t = (l, "test")
print(t)
t[0][0][0] = 1.0
print(t)

d = {(1,2,3):("one, two, three")}
print(d)
print(d[(1,2,3)])

# d[t] = "test" error

l = (1,2,3)
m = (1,2,3)
print(l is m)

l = [1,2,3]
m = [1,2,3]
print(l is m)

# s1 = "test"
# s2 = "test"
# s3 = "te"+"st"
# s4 = input("input 'test':\n")
# print(s1 is s2 is s3 is s4)
# print(id(s1), id(s2), id(s3), id(s4))

a = 5
b = 5
print(a is b)

a = 500
b = 500
print(a is b)

a = 5
b = int(input("input 5:\n"))
print(a is b)

a = 500
b = int(input("input 500:\n"))
print(a is b)