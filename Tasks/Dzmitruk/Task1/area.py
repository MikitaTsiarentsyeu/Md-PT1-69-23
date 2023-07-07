# a program which calculates the area of a circle given its radius

import math

rad = input("Enter the radius of circle: ")

if not rad.isdecimal():
    print ("Your enter wrong radius")
    exit()
 
rad = float(rad)

if rad == 0:
    print ("Your enter wrong radius")
    exit()

if rad > 0:
    area = math.pi*rad**2
    print ( f"The area of circle with radius { rad }  is  {area: .2f} ")

