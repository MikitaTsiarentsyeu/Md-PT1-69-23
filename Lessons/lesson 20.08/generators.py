def test_gen():
    yield 1
    yield 2
    yield 3

g = test_gen()
print(g)
print("the end")

for i in g:
    print(i)

def even_cubes(n):
    for i in range(n):
        if i % 2 == 0:
            yield i**3

print([x for x in even_cubes(100)])