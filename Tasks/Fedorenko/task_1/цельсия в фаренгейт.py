celcius=str(input('enter degrees Celsius:\n'))

if not celcius.isdigit():
    print("Your input was not an integer number")
    exit()

celcius = float(celcius)
x=9/5
y=32
print(x*celcius+y)