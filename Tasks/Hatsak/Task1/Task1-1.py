def askToExit():
    print("Do you want to exit program?")
    print("Enter 'Y' to say 'yes', 'N' to say 'no'")
    answer = input()
    if answer.upper() == 'N':
        return True
    elif answer.upper() == 'Y':
        return False
    else:
        return askToExit()


print("Hello! This program converts Celsius to Fahrenheit")
flag = True

while flag:
    cel = input("Enter value in Celsius\n")
    far = 1.8 * float(cel) + 32
    print(far)
    flag = askToExit()





