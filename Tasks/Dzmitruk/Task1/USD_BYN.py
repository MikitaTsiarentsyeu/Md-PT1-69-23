# a program which converts some amount of money from USD to BYN

course = 3.07

usd = input("Enter amount of money in USD: ")

if usd.isalpha():
    print ("Your enter wrong amount.")
    exit()    
 
usd = float(usd)

if usd > 0:

    byn = usd * course
    print(f"Amount of money in BYN is {byn: .2f}" )
