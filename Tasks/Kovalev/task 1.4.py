#Hi this is a program that can convert USD in BYN
rate = 2.52
USD = input('please enter a number in USD\n')
USD = float(USD)
BYN = USD * rate 
print(BYN)
print(f'{USD}USD is {BYN}BYN')
