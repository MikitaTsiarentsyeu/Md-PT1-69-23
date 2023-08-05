x, y = [2], [3]

def test_args(a, b):
    a[0]=a[0]+2
    b[0]=b[0]+3
    print(id(a), id(b))
    print(a, b)

print(id(x), id(y))
test_args(x, y)
print(id(x), id(y))

def three_args(a, b, c):
    print(a, b, c)

three_args("first", "second", "third")
three_args(b="first", c="second", a="third")

def my_join(coll, sep=',', mult=3):
    return sep.join(coll)*mult

print(my_join(["1","2","3"]))
print(my_join(["1","2","3"], '|'))
print(my_join(["1","2","3"], '|', 5))
print(my_join(["1","2","3"], mult=10))

print(1,2,3,4,5,"test", sep=',', end='.\n')

def sum(*values):
    print(*values)
    res = 0
    for num in values:
        res += num
    return res

print(sum(1,2,3,4,5,6,7,8,9,10))
print(sum(*[1,2,3,4,5]))

def my_print(*args, sep=',', end='.\n'):
    print(*args, sep=sep, end=end)

my_print(1,2,3,4,5,sep='-',end='!\n')

def my_print(**kwargs):
    print(*(kwargs['args']), sep=kwargs['sep'], end=kwargs['end'])

# my_print(one=1,two=2,three=3,four=4,five=5)
# my_print(**{"1":"one", "2":"two"})

my_print(args=[1,2,3,4,5],sep=',',end='.\n')


def test_func(a, b, c, *args, **kwargs):
    pass