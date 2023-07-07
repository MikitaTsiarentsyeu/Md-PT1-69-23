
# a program which converts Celsius to Fahrenheit.

t_celsius = input ("Enter the temperature in Celsius: ")

if t_celsius.isalpha():
    print ("Your enter a wrong data.")
    exit()

t_celsius = float ( t_celsius )

t_fahrenheit = t_celsius * 1.8 + 32

print(f"Your temperature in Fahrenheit is {t_fahrenheit} ")

