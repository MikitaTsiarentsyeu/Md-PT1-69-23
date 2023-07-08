def isfloat(data):
    try:
        float(data)
        return True
    except ValueError:
        return False

USD = (input("Enter your amount in USD: \n"))

if isfloat(USD) == False:
    print("Please enter correct USD value")
    exit()

ratio = (input("Enter your currency ratio for BYN (for example, 1 USD is 2 BYN, enter 2 etc.): \n"))

if isfloat(ratio) == False:
    print("Please enter correct ratio value")
    exit()

USD = float(USD)
ratio = float(ratio)

BYN = USD*ratio
print(f"Your amount of money BYN:\n{BYN}") 