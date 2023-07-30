from decimal import Decimal, InvalidOperation


# Since isdecimal() works not as how I expected
# (e.g.: "32.4".isdecimal() -> False)
# I need to do my own function
def isitdecimalable(x):
    try:
        x = Decimal(x)
        return True
    except InvalidOperation:
        return False


c = input("Put your Celsius value: ")

while not isitdecimalable(c):
    c = input("Invalid input, please try again: ")

f = Decimal(c) * 9 / 5 + 32
print(f"{c} Celsius is {f} Fahrenheit")
