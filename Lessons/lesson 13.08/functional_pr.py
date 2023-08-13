from functools import reduce

def apply(l, f):
    for i in l:
        f(i)

apply(range(10), print)

def to_lower(x):
    return x.lower()

test_str = "Abc Aac aaa kkk"
lst = test_str.split()
print(sorted(lst, key=str.lower))
print(lst)

print(sorted(lst, key=to_lower))

def sorting_key(x):
    return x[1]

l = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(l, key=sorting_key))

def sum(x, y):
    return x+y

sum = lambda x, y: x+y
print(sum(2, 3))

print((lambda x, y: x+y)(2, 3))

l = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(l, key=lambda x: x[1]))

l = [1,2,3,4,5,6,7,8,9,10]
x = map(print, l)
print(x, type(x))
print(list(x))

print(list(map(lambda x: chr(x*10), l)))

print(list(map(str, l)))

print(list(filter(lambda x: x>4, l)))

print(list(map(lambda x: chr(x*10), filter(lambda x: x>4, l))))

print(reduce(lambda x, y: x+y, l))

print(reduce(lambda x, y: f"{x}-{y}", l))
"1-2"
"1-2-3"
"1-2-3-4"

print(reduce(lambda x, y: x if x >= y else y, l))