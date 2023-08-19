number = input('Please, input the number:\n')

try:
    number = float(number)
except:
    print('Your input of number is incorrect!')
    exit()

power = input('Please, input the power:\n')

try:
    power = int(power)
except:
    print('Enter the power as an integer!')
    exit()


def power_of_number(number, power):
    if power == 1:
        return number
    if number == 0 and power < 0:
        return "Raising zero to a negative power doesn't make sense"
    if power == 0:
        return 1
    if power > 0:
        return number * power_of_number(number, power - 1)
    if power < 0:
        return 1/number * power_of_number(number, power + 1)


print(f'{number} in power {power} is: {power_of_number(number, power)}')

