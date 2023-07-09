l = []
print(type(l), l)
print(len(l))

l = [1.0,2,3,4,5,6,7,8,9,'10']
print(type(l), l)
print(len(l))

print(l[0], l[-1], l[2:7:2], l[::-1])

print([1,2,3]+[4,5,6])
print([1,2,3] + list("456"))
print([0]*8)

l[0] = 0.1
print(l)

# l[1000] = 1000 error

l.append("last elem")
print(l)
l.append("new last elem")
print(l)

l.extend("test")
print(l)

l.insert(0, "new first elem")
print(l)

l[0:2] = [1,2,3,4,5]
print(l)

l.remove(2)
print(l)

# l.remove(20) error
# print(l)

print(1 in l)
print(100 in l)

print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)

print(l.pop(0))
print(l)
print(l.pop(0))
print(l)
print(l.pop(0))
print(l)

del l[0]
print(l)

del l[:6]
print(l)

del l[:]
print(l)

a = "test str"
l.append(a)
print(l)
del l[0]
print(l)
print(a)

l.clear()
print(l)

# del l 
# print(l)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(id(l1), id(l2))
print(l1 == l2)

l = [1, 2, 3]
new_l = list(l)

l[0], l[1] = l[1], l[0]
print(l)