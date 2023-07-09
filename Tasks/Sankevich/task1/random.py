import random

number1 = input('thats number lower')
number2 = input('thats number higher')

while number1.isdigit() == False: 
    number1 = input('gimme NUMBER')


while number2.isdigit() == False:
    number2 = input('gimme NUMBER')



while float(number2) <= float(number1):
    number2 = input('gimme number higher')

number1 = float(number1)
number2 = float(number2)

print(random.randrange(number1, number2))