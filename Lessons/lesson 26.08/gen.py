
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        yield a
        count += 1
        if count == n:
            return
        a, b = b, a+b

# f_g = fibonacci(10)

# for i in f_g:
#     print(i)

f_g = fibonacci(10)
# print(len(f_g))

gen_iter = iter(f_g)
empty = False
try:
    next(gen_iter)
except StopIteration:
    empty = True

if not empty:
    for i in fibonacci(10):
        print(i)


l = [1,2,[3,3.0,["three"]],4,5,6]

# def flatten(l):
#     for i in l:
#         if isinstance(i, list):
#             flatten(i)
#         else:
#             print(i)

def flatten(l):
    for i in l:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i

flat_gen = flatten(l)
for i in flat_gen:
    print(i)



res = (x for x in range(10))
print(res)

for i in res:
    print(i)


(x for x in range(10))
[x for x in range(10)]