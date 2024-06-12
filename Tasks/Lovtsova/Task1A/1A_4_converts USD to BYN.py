#4.Write a program that converts some amount of money from USD to BYN, the amount and ratio are given.

import decimal

u = input("Please, enter your amount of money in USD:\n")
c = input("Today, the ruble exchange rate is:\n")

try:
    u=float(u)
    c=float(c)
    b=round(decimal.Decimal(u*c),2)
    print(u," USD is",b," BYN")
except ValueError:
    print("It's not correct data! Please, enter again!")