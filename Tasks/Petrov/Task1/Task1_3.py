from decimal import Decimal


def isitspeed(x):
    try:
        x = Decimal(x) > 0
        if x:   # if-else -> return x
            print("Alright")
            return True
        else:
            print("Speed cant be negative or 0")
            return False
    except:
        print("Invalid input")
        return False


s = input("Put your speed value (in km/h): ")

while not isitspeed(s):
    s = input("Please try again: ")
        
f = Decimal(s) * 1000 / 3600
print(f"When your speed is {s} km/h, it is equal to {round(f,2)} m/s")