import decimal
import fractions
import math

x = 3
print(type(x))

y = -2.9
print(int(y))

print(4/2)
print(5//2)

y = 5/2
print(type(y), y)

print(1.1+1.1+1.1)

print(1.4+2.5)

print(float(5))

print(round(2.5))
print(round(3.5))
print(round(4.5))

print(decimal.Decimal(1.1)+decimal.Decimal(1.1)+decimal.Decimal(1.1))
print(decimal.Decimal(1.1))
print(decimal.Decimal('1.1'))

x = decimal.Decimal('1.1')
print(type(x))
print(x+x+x)

x = fractions.Fraction('1.5')
print(x*x)

print(999999999999999999999999>-math.inf)

print(math.inf==math.inf)
print(math.nan==math.nan)