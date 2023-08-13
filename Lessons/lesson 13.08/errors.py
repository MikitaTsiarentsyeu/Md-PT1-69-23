x = 5

try:
    xx.lower()
    print("something else")
except AttributeError:
    print("it's not str")
except:
    print("мама, я упал")

while True:
    try:
        i = input("enter str value")
        2 + int(i)
        break
    except ValueError:
        print("you have entered invalid value, please try again")