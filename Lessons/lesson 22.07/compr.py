l = [1,2,3,4,5]

print([str(x) for x in l])

# test = []
# for x in l:
#     test.append(str(x))
# print(test)

print({str(x) for x in l})
print({x:str(x) for x in l})

print([x for x in range(100)])

print([x**10 for x in range(100)])

print([x**2 if x % 2 == 0 else x**3 for x in range(100)])

print([ord(x) for x in "test str"])

v = "eioayu"

print(''.join(['' if x in v else x for x in "test str"]))

print(''.join([x for x in "test str" if x not in v]))

l = [[1,2,3], [4,5,6], [7,8,9]]
print([y for x in l for y in x])