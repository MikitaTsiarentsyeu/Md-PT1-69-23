"""Write a program that converts kilometers per hour to meters per second, ask a user for the speed"""

print("Welcome to km/h to m/s converter.")

kmh = input("Please, enter the speed, km/h:\n")

if not kmh.isdigit() and '.' not in kmh:
    print("Your input is incorrect. Please, enter a numeric value.")
    exit()

kmh = float(kmh)
ms = kmh * (1000 / 3600)
ms = round(ms, 2)
print("The speed is", ms, "m/s")