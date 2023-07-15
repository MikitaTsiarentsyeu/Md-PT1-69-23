s = {1,2,3}
print(s, type(s))

s = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
print(s)

s = {}
print(s, type(s))

s = set()
print(s, type(s))

l = [1,1,2,2,3,4,56,7,5,3,2,2,3,5,6,7,43,2,7]
print(set(l))

s = "test str"
print(set(s))

l = list(set(l))
print(l)

s = ''.join(set(s))
print(s)

l1 = [1,2,2,2,2,2,2,3]
l2 = [3,2,1]
print(set(l1) == set(l2))

l = ['s','e','t']
s = "set"
print(set(l) == set(s))

s = {1,2,3,4,5}
s.add(1)
print(s)
s.add("test")
print(s)

s.update("test")
print(s)

s.remove(5)
print(s)

if 5 in s:
    s.remove(5)
    print(s)

s.discard(5)
print(s)

# s[1] error

print(s.pop())
print(s.pop())
print(s)

s.clear()
print(s)

print({1,2,3}.union({3,4,5}))
print({1,2,3}.intersection({3,4,5}))

print({1,2,3}.issubset({1,2,3,4,5}))