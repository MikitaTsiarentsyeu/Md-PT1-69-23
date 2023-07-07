from math import pi
r = input("Please, input the radius of the circle in centimeters:\n")
try:
    r = float(r)
    if r > 0:
        square = pi * r**2
        print(f"The area of the circle is {square} square centimeters")

    else:
        print("Your input is incorrect")
except:
    print("Your input is incorrect")