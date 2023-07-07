# 2. Write a program that calculates the area of a circle given its radius, ask a user for the radius.

import math

radius = input("Enter the radius of the circle :\n")
try:
    radius = float(radius)
except ValueError:
    print("Data entry error.")
    exit()

area = math.pi * radius ** 2
rounding = round(area, 2)
print("Area of a circle:", rounding)
