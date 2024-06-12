#3.Write a program that converts kilometers per hour to meters per second, given the speed in kilometers per hour.

kh = input("Enter the kilometers per hour (integer):\n")

try:
    kh=float(kh)
    if kh>=0:
        ms=round((kh*0.278),2)
        print(kh, "k/h (kilometers per hour) is" , ms, "m/s (meters per second)\n")
    else:
        print("The speed cannot be negative!\n")
except:
    print("This is some kind of bullshit!\n")