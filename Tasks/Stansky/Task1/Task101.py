
temperature = input('Enter temperature in degrees Celsius\n')
try:
    temperature = float(temperature)
    F = (1.8 * temperature) + 32
    print(f'The temperature is {F} in Fahrenheit')
except:
    print('Your input was not integer number')




