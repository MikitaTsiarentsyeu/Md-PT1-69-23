# 4. Write a recursive function to calculate the power of a given number.

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else:
        return 1 / power(base, -exponent)

print(power(2, 3))
