import random
import decimal

def checkNumber(value):
    try:
        return float(value)
    except ValueError:
        print('Invalid value, try again...')
        exit()

value = input("Converter USD to BYN:\nEnter quantity USD: ")
szValue = checkNumber(value)
if szValue > 0:
    kurs = random.uniform(2.95, 3.1)
    convert = decimal.Decimal(szValue*kurs)
    print(f"""Kurs: 1 USD / {round(kurs, 2)} BYN""")
    print(f"""At the rate {szValue} USD = {round(convert, 2)} BYN""")
else:
    print('Invalid value, try again...')