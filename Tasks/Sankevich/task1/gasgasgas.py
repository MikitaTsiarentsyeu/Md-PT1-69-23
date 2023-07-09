kph = input('gimme kph: ')
while kph.isdigit() == False:
    kph = input()

kph = float(kph)

mps = kph * (1000 / 3600)
print(mps)