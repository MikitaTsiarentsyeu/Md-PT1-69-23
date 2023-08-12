from decimal import Decimal, InvalidOperation, DivisionByZero


def power(number, pow_count):
    if pow_count == 1:
        return number
    elif pow_count:
        return number * power(number, pow_count-1)
    else:
        return 1


while True:
    try:
        num = Decimal(input("Input a number: "))
        break
    except InvalidOperation:
        print("This input should be a number")
        continue

while True:
    try:
        pow = int(input("Input a power: "))
        break
    except ValueError:
        print("This input should be an integer number")
        continue

try:
    result = 1/power(num, -pow) if pow < 0 else power(num, pow)
    print(f"{num} in power {pow} is {result}")
except DivisionByZero:
    print(f"{num} in power {pow} is infinity")
