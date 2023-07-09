import math

radius = input('gimme radius: ')
while radius.isdigit() == False:
    radius = input()

radius = float(radius)

area = radius * math.pi ** 2

print('here is your area: ', area)