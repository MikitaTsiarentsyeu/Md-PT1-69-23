celsius = input('gimme nuber of your celsius: ')
while celsius.isdigit() == False:
    celsius = input('gimme nuber of your celsius: ')

celsius = float(celsius)
fr = (celsius * 9 / 5) + 32
print("here's your фаренгейт: ", fr)
