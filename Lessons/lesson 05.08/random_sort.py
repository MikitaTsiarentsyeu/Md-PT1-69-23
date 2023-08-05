import random

l = [4,2,4,6,8,9,5,3,12,5,1]

def random_sort(l):
    n = len(l)
    count = 0
    while not is_sorted(l):
        i = generate_index(n)
        j = i
        while j == i:
            j = generate_index(n)
        swap(l, i, j)
        count += 1
    print(count)

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def generate_index(n):
    return random.randint(0, n-1)

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

random_sort(l)
print(l)
