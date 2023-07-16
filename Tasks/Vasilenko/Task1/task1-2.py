"""Write a program that calculates the area of a circle given its radius, ask a user for the radius"""

import math

print("Welcome! Here you can calculate the area of a circle.")

rad = input("Please, enter the value of the circle's radius:\n")
measure = input("Please, enter the measure of length (m, cm, in, ft etc.):\n")

if not rad.isdigit() and '.' not in rad:
    print("Your input is incorrect. Please, enter a numeric value.")
    exit()

rad = float(rad)
area = (rad ** 2) * math.pi
area = round(area, 2)
print("The area of the circle is", area, measure+'²')
