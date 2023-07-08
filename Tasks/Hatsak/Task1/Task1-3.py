"""3.Write a program that converts kilometers per hour to meters per second, ask a user for the speed."""

print("Hello! This program will convert your speed from kilometers per hour to meters per second")
print("Enter your speed:", end=' ')


def enter():
    speed = input()
    try:
        speed = float(speed)
        return speed
    except:
        print("Invalid input! Try again!")
        return enter()


speed = enter()
answer = round(int(speed)*1000/3600, 2)
print(f"{speed} km/h = {answer} m/s")
