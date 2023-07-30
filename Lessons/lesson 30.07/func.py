def sum(a, b):
    hello("test")
    res = a+b
    return res

def hello(name):
    print(f"hello, {name}")

x = sum(2, 3)
print(x)
sum(4, 7)
sum(-4, 8)

hello("test")

print(type(print), type(sum))
print(id(print), id(sum))
print(isinstance(sum, object))

sign = "+"
if sign == "+":
    def func(a, b):
        return a+b
elif sign == "*":
    def func(a, b):
        return a*b

def func(a, b, sign):
    if sign == "+":
        return a+b
    elif sign == "*":
        return a*b
    return "undefined"

func(2, 3, "*")

def test_args(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")

test_args("first", "third", "second")

def test_list(a):
    print(id(a))
    a.append("new elem")

l = [1,2,3,4,5]
print(id(l))
test_list(l)
print(l)

def test_int(a):
    print(id(a))
    a += 2
    print(id(a))

val = 5
test_int(val)
print(val, id(val))

def test_return():
    print("before return")
    return 2,3
    print("after retun")

a, b = test_return()
print(a, b)