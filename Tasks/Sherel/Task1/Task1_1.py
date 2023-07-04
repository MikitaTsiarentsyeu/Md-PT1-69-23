def checkNumber(celsius):
    try:
        return float(celsius)
    except ValueError:
        print('Invalid value, try again...')
        exit()

celsius = input("Converter Celsius to Fahrenheit\nEnter a number in °C: ")
szCelsius = checkNumber(celsius)
convertFahrenheit = (float(szCelsius) * 9/5) + 32
print(f"""{format(float(celsius), '.1f')} °C is {format(float(convertFahrenheit), '.1f')} °F""")