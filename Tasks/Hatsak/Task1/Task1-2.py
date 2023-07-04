"""2.Write a program that calculates the area of a circle given its radius, ask a user for the radius."""
import math

print("Hello! This program will calculate the area of a circle! Give me a radius!")
radius = input()

if radius.isdigit():
    print("The area of your circle is: ", round(int(radius)**2 * math.pi, 2))
elif '.' in radius[1:-1] and radius.count('.') == 1 \
        and (radius[0:radius.index('.')] + radius[radius.index('.')+1:]).isdigit():
    print("The area of your circle is: ", round(float(radius)**2 * math.pi, 2))
else:
    print("Please, enter only integer or float values."
          " Use '.'-symbol to separate the fractional part in float numbers.")
    exit()