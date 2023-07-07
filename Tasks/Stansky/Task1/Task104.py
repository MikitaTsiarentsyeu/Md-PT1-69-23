rate = 3.05
money = input('Please, input the amount in USD:\n')
try:
    money = float(money)
    if money >= 0:
         currency = money*rate
         print(f'{money} USD is {currency} BYN')
    else:
        print('Your input is incorrect')

except:
    print('Your input is incorrect')