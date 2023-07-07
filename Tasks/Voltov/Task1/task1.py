# 1. Write a program that converts Celsius to Fahrenheit, ask a user for the Celsius value.


Celsius = input("Enter temperature in Celsius :\n ")
try:
    Celsius = float(Celsius)
except ValueError:
    print("Data entry error.")
    exit()

Fahrenheit = Celsius * (9 / 5) + 32
print("Temperature in Fahrenheit: ", Fahrenheit)


