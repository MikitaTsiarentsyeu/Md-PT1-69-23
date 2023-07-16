"""Write a program that converts some amount of money from USD to BYN,
ask a user for the amount, store the ratio inside the program itself."""

print("Welcome to USD to BYN currency converter!")

usd = input("Please, enter the amount of money in USD:\n")

if not usd.isdigit() and '.' not in usd:
    print("Your input is incorrect. Please, enter a numeric value.")
    exit()

exch_rate = 3.0291

usd = float(usd)
byn = usd * exch_rate
byn = round(byn, 2)
print("The amount in BYN is", byn)
