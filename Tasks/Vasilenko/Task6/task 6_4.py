"""Write a recursive function to calculate the power of a given number"""

input_number = input("Please, enter the number:\n")
input_power = input("Please, enter the power you want to calculate:\n")


def calculated_power(number, power):
    if power == 0:
        return 1
    elif power > 0:
        if power == 1:
            return number
        else:
            return number * calculated_power(number, power-1)
    else:
        if power == -1:
            return 1/number
        else:
            return (1/number) * calculated_power(number, power+1)


print(f'Your number raised to the given power is {calculated_power(input_number, input_power)}')
