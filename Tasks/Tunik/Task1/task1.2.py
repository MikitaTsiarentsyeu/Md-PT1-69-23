import math

def isfloat(data):
    try:
        float(data)
        return True
    except ValueError:
        return False

r = (input("Enter your radius value: \n"))

if isfloat(r) == False:
    print("Please enter correct raduis value")
    exit()

r = float(r)
 
S = math.pi*r**2
print(f"Your value of the area:\n{S}") 