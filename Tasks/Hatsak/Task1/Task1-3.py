"""3.Write a program that converts kilometers per hour to meters per second, ask a user for the speed."""

print("Hello! This program will convert your speed from kilometers per hour to meters per second")
print("Enter your speed:", end=' ')
speed = input()
answer = int(speed)*1000/3600
print(f"{speed} km/h = {answer} m/s")
