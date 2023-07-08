# a program which converts kilometers per hour to meters per second.

speed_kph = input ("Enter the speed in kilometers per hour: ")

if not speed_kph.isdecimal():
    print ("Your enter wrong speed")
    exit()
 
speed_kph = float(speed_kph)

if speed_kph >= 0:
    speed_mps = speed_kph / 3.6
    print ( f"Your speed is{speed_mps: .2f} meters per second." )


