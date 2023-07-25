#4.Write a program that converts some amount of money from USD to BYN, the amount and ratio are given.
import decimal

u = float(input("Please, enter your amount of money in USD:\n"))
c = float(input("Today, the ruble exchange rate is:\n"))
b = round(decimal.Decimal(u*c),2)

print(u," USD is",b," BYN")
