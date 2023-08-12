
def counter(n):
    def inner():
        nonlocal n
        n+=1
        return n
    return inner

from10 = counter(10)
from100 = counter(100)

print(from10())
print(from100())
