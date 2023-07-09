t = ()
print(type(t), t)

t = (1,)
print(type(t), t)

t = (1.0,2,3,4,5,"test",[])
print(t)

print(t[0], t[:4:2])
print((1,2,3)+(4,5,6))

# t[0] = 0 error

print((0,) + t[1:])