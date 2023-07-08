radius = float(input("enter radius:\n"))

if radius <= 0:
    print('wrong')
    exit()

pi=3.14
x=2
print(pi*(radius**x))