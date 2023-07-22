l = [2,54,67,8,65,3,2,34,56,6,43]

# print(sorted(l))
# print(l)

# l.sort()
# print(l)

is_sorted = True

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        is_sorted = False
        break

print(is_sorted, i)


for j in range(len(l)-1):
    for i in range(len(l)-j-1):
        if l[i] > l[i+1]:
            l[i+1], l[i] = l[i], l[i+1]

    print(l)

l = [54,67,8,65,3,2,34,56,6,43]

for j in range(len(l)-1):
    current_idx = j
    min_idx = current_idx
    for i in range(current_idx, len(l)):
        if l[i] < l[min_idx]:
            min_idx = i
        
    l[current_idx], l[min_idx] = l[min_idx], l[current_idx]
    print(l)

