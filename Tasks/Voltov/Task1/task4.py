# 4. Write a program that converts some amount of money from USD to BYN,
# ask a user for the amount, store the ratio inside the program itself.

usd = input("Enter the amount in US dollars:\n ")
try:
    usd = float(usd)
except ValueError:
    print("Data entry error.")
    exit()
exchange_rates = 3.05
byn = usd * exchange_rates
print(f"{usd} US dollars are equal {byn} Belarusian rubles")