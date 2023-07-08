"""1.Write a program that converts Celsius to Fahrenheit, ask a user for the Celsius value."""
def askToExit():
    print("Do you want to exit program?")
    print("Enter 'Y' to say 'yes', 'N' to say 'no'")
    answer = input()
    if answer.upper() == 'N':
        return True
    elif answer.upper() == 'Y':
        print('Goodbye!')
        return False
    else:
        return askToExit()


print("Hello! This program converts Celsius to Fahrenheit")
flag = True

while flag:
    cel = input("Enter value in Celsius, °C\n")
    if not cel.isdigit():
        print("ERROR! Only integers valid!")
        continue
    far = 1.8 * float(cel) + 32
    print(far, '℉')
    flag = askToExit()





