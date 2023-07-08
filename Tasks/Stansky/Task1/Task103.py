V = input("Please, input speed in kilometers per hour:\n")
try:
    V = float(V)
    if V >= 0:
        speed = V*1000/3600
        print(f"Speed in meters per second is {speed}")
    else:
        print("Your input is incorrect")

except:
    print("Your input is incorrect")