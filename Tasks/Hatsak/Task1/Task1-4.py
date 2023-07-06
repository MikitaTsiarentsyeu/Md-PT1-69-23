"""4.Write a program that converts some amount of money from USD to BYN,
 ask a user for the amount, store the ratio inside the program itself."""
import requests
response = requests.get("https://api.nbrb.by/exrates/rates/USD?parammode=2")
curr = response.json()['Cur_OfficialRate']
print("Hello! This program will convert USD to BYN")


def calculate():
    value = input("Enter your BYN: ")
    try:
        value = float(value)
        return value
    except:
        print("Please, enter only positive integer or float values.")
        return calculate()


value = calculate()
print(f"{value} BYN = {round(value/curr, 3)} USD")