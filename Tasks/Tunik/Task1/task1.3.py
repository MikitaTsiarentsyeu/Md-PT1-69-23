def isfloat(data):
    try:
        float(data)
        return True
    except ValueError:
        return False

Kmh = (input("Enter your speed in kilometers per hour: \n"))

if isfloat(Kmh) == False:
    print("Please enter correct speed value")
    exit()

Kmh = float(Kmh)
 
ms = Kmh/3.6
print(f"Your speed value in meters per second:\n{ms}") 