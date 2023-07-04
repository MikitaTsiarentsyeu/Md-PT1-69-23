import decimal
from math import pi, pow

def checkNumber(radius_mm):
    try:
        return float(radius_mm)
    except ValueError:
        print('Invalid value, try again...')
        exit()

radius = input("Program is Area of a circle:\nEnter a number in mm [from 1 to +∞]: ")
szRadius = checkNumber(radius)
if szRadius > 0:
    area_mm = pi*pow(szRadius, 2)
    area_sm = area_mm/100
    area_m2 = float(area_sm/10000)
    area_m2 = decimal.Decimal(area_m2)
    print(f"""Result:\n{szRadius} mm = {round(area_mm, 2)} mm²\n{szRadius} mm = {round(area_sm, 4)} sm²\n{szRadius} mm = {round(area_m2, 7)} m²""")
else:
    print('Invalid value, try again...')