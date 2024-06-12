# 2.Write a program that calculates the area of a circle given its radius.

your_radius = input("Enter the radius value (integer in meters):\n")

try:
    your_radius=float(your_radius)
    your_area = round((3.1428*((your_radius)**2)),2)  
    print("The area of a circle value is",your_area," m2")

except ValueError:
    print("This is some kind of bullshit!\n")