def calculate(number,power):
    if power == 0:
        return 1
    return (number*calculate(number,power-1))
print(calculate(number=3,power=5))