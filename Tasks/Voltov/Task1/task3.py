# 3. Write a program that converts kilometers per hour to meters per second, ask a user for the speed.

km = input("Enter speed in kilometers per hour: \n")
try:
    km = float(km)
except ValueError:
    print("Data entry error.")
    exit()
meters = km * 1000 / 3600
rounding = round(meters, 2)
print("Speed in meters per second:", rounding)

