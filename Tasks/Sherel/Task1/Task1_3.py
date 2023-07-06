def checkNumber(speed):
    try:
        return float(speed)
    except ValueError:
        print('Invalid value, try again...')
        exit()

speed = input("Converter km/h to m/s:\nEnter a speed in km/h: ")
szSpeed = checkNumber(speed)
if szSpeed > 0:
    convert = szSpeed*1000/3600
    print(f"""{szSpeed} km/h = {round(convert, 5)} m/s""")
else:
    print('Invalid value, try again...')