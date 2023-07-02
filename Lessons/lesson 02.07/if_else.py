number = int(input("Enter some number:\n"))

if number == 1:
    print("the number is one")
elif number == 2:
    print("the number is two")
elif number == 3:
    print("the number is three")
else:
    print("idk this number")



if number == 0 or number > 0:
    if number == 0:
        print("it's zero")
    else:
        print("the number is positive")
        print("I'm sure")
elif number < 0:
    print("the number is negative")

print("the end")