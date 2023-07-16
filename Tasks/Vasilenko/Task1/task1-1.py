"""Write a program that converts Celsius to Fahrenheit, ask a user for the Celsius value"""

print("Welcome to Celsius to Fahrenheit temperature converter!")

cels = input("Please, enter the temperature in Celsius, °C:\n")


if not cels.isdigit() and '.' not in cels:
    print("Your input is incorrect. Please, enter a numeric value.")
    exit()

cels = float(cels)
fahr = (cels * 1.8) + 32
fahr = round(fahr, 2)

print("The temperature in Fahrenheit is", fahr, "℉")
