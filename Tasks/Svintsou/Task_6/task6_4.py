def power(number, rate):
    if rate == 1 or number < 2:
        return number

    return number * power(number, rate - 1)


print(power(2, 4))