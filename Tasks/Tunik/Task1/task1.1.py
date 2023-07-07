def isfloat(data):
    try:
        float(data)
        return True
    except ValueError:
        return False

Celsius = (input("Enter your Celsius value: \n"))

if isfloat(Celsius) == False:
    print("Please enter correct Celsius value")
    exit()

Celsius = float(Celsius)
 
Fahrenheit = Celsius*9/5+32
print(f"Your Fahrenheit value:\n{Fahrenheit}") 