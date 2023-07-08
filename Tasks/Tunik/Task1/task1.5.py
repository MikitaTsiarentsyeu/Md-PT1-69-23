import random

def isfloat(data):
    try:
        float(data)
        return True
    except ValueError:
        return False

Left = (input("Enter your value for Left border: \n"))

if isfloat(Left) == False:
    print("Please enter correct value for Left border")
    exit()

Right = (input("Enter your value for Right border: \n"))

if isfloat(Right) == False:
    print("Please enter correct value for Right border")
    exit()

Left = float(Left)
Right = float(Right)

random_number = random.uniform(Left,Right)
print(f"Your random number:\n{random_number}") 