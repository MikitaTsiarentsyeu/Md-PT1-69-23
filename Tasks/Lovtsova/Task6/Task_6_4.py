def calculate_power(number:float, power:int)->float:
    """4.The recursive function to calculate 
    the power of a given number"""
    if number == 0 and power < 0:
        return "На 0 делить нельзя! Возведение нуля в любую отрицательную степень не имеет смысла, т.е. результат не определён!!!"
    elif power == 0:
        return 1
    elif power>0:
        return number*calculate_power(number, power-1)
    elif power<0:
        return 1/number*calculate_power(number, power+1)
    else:
        print("Что-то пошло не так!")

while True:
    try:
        number=float(input("Please, enter your number (integer or float):\n"))
        break
    except ValueError:
        print ("\t\t Please, try again!")
        continue
    
while True:
    try:
        power=int(input("Please, enter your power (integer):\n"))
        break
    except ValueError:    
        print ("\t\t Please, try again!")
        continue

print(f'\tThe {number} in power {power} is {calculate_power(number, power)}')