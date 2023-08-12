a, b = 3, 4
l = []

def test_func(a, b):
    print(a, b)
    a, b = 44, 55
    print(a, b)

test_func(1,2)
print(a, b)

def test_global_scope():
    print(a, b)
    l = [0]
    print(l)

test_global_scope()

i = "test"

for i in range(10):
    i+=1

print(i)

i = "test"

[i for i in range(10)]

print(i)

def test_one(a):
    print(a)

def test_two(a):
    print(a)

test_one(1)
test_two(2)


# global_variable = "global test"

def modify_global():
    global global_variable
    global_variable = "new global value"
    print(global_variable)

modify_global()
print(global_variable)