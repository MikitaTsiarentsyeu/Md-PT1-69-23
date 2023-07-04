def checkNumber(celsius):
    try:
        return float(celsius)
    except ValueError:
        print('Invalid value, try again...')
        exit()

celsius = input("Converter Celsius to Fahrenheit\nEnter a number in °C: ")
szCelsius = checkNumber(celsius)
convertFahrenheit = (szCelsius * 9/5) + 32
print(f"""{format(szCelsius, '.1f')} °C is {format(convertFahrenheit, '.1f')} °F""")