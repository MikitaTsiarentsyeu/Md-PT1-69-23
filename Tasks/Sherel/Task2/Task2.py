"""Implement a text output of the time entered from the console (the user should input data in the format hh:mm).

Show the responses to the user in Russian according to the rules listed below:

min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
min == 30: половина такого-то (15:30 - половина четвёртого)
min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
min >= 45 без min такого-то (08:54 - без шести минут девять)"""

from db import myList

user_time = input("Enter your data in the format (hh:mm):\n")
user_time = user_time.replace(':', '')

#input check 4 time values
if len(user_time) != 4:
    print("your input has incorrect format")
    exit()

#I assign each digit of the time to the variable h*
h1, h2, m1, m2 = user_time[0], user_time[1], user_time[2], user_time[3]

#checking that the user entered input integers
if not h1.isdigit() or not h2.isdigit() or not m1.isdigit() or not m2.isdigit():
    print("your input has incorrect format")
    exit()

h1, h2, m1, m2 = int(h1), int(h2), int(m1), int(m2) #change the data type for each variable h*
hh = int(user_time[0:2]) #assign the hour digits to a variable hh
mm = int(user_time[2:4]) #assign the minutes digits to a variable mm

#check if input is in 24h range
if hh > 23 or m1 > 5 or m2 > 9:
    print("your input has incorrect format")
    exit() #

#I simplify my task, I translate the 24h format into 12h
if int(user_time[0:2]) > 12:
    hh -= 12

#Ifulfill the condition for the correct output of the end of hours
if hh == 1:
    hhText = myList["hh"][0]
elif hh <= 4 and hh > 1:
    hhText = myList["hh"][1]
elif hh <= 12 and hh > 4:
    hhText = myList["hh"][2]
elif hh == 0:
    hhText = myList["hh"][2]

#first condition
#min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
if mm == 0:
    print(f"""{myList[hh][0]} {hhText} {myList[0][0]}""")
    exit()

#second condition
#min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
if m2 == m2:
    if m2 == 1:
        mmText = myList["mm"][0]
    elif m2 <= 4 and m2 > 1:
        mmText = myList["mm"][1]
    elif m2 <= 9 and m2 >= 5:
        mmText = myList["mm"][2]
    elif m2 == 0:
        mmText = myList["mm"][2]

if mm < 30:
    if mm >= 16 and mm <= 19:
        print(f"""{myList[m2][0][:-1]+myList["suff"][0]} {myList["mm"][2]} {myList[hh + 1][1]}""")
        exit()
    if mm >= 10 and mm < 20:
        print(f"""{myList[m1][0][:-1]+myList["suff"][0]} {myList["mm"][2]} {myList[hh + 1][1]}""")
        exit()
    if mm == 20:
        print(f"""{myList[m1][0][:-1]+myList["suff"][1]} {myList["mm"][2]} {myList[hh + 1][1]}""")
        exit()
    if mm > 20:
        if m2 == 1 or m2 == 2:
            print(f"""{myList[m1][0]+myList["suff"][1]} {myList[m2][3]} {mmText} {myList[hh + 1][1]}""")
            exit()
        print(f"""{myList[m1][0]+myList["suff"][1]} {myList[m2][0]} {mmText} {myList[hh+1][1]}""")
        exit()
    if 0 < mm:
        if mm == 1 or m2 == 2:
            print(f"""{myList[m2][3]} {mmText} {myList[hh + 1][1]}""")
            exit()
        print(f"""{myList[m2][0]} {mmText} {myList[hh+1][1]}""")
        exit()

#third condition
# min == 30: половина такого-то (15:30 - половина четвёртого)
if mm == 30:
    print(f"""{myList[0][1]} {myList[hh + 1][1]}""")
    exit()

#fourth condition
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
if mm > 30 and mm < 45:
    if mm == 40:
        print(f"""{myList[m1 * 10][0]} {mmText} {myList[hh + 1][1]}""")
        exit()
    if mm > 40 and mm < 45:
        if m2 == 1 or m2 == 2:
            print(f"""{myList[40][0]} {myList[m2][3]} {mmText} {myList[hh + 1][1]}""")
            exit()
        print(f"""{myList[40][0]} {myList[m2][0]} {mmText} {myList[hh + 1][1]}""")
        exit()
    if mm > 30 and mm < 40:
        if m2 == 1 or m2 == 2:
            print(f"""{myList[m1][0] + myList["suff"][1]} {myList[m2][3]} {mmText} {myList[hh + 1][1]}""")
            exit()
        print(f"""{myList[m1][0]+myList["suff"][1]} {myList[m2][0]} {mmText} {myList[hh + 1][1]}""")
        exit()

#fifth condition
#min >= 45 без min такого-то (08:54 - без шести минут девять)
if mm >= 45:
    if hh == 12:
        myList[hh + 1][0] = myList["hh"][0]
    if 60-mm >= 5 and 60-mm <= 15:
        print(f"""{myList[0][2]} {myList[60-mm][0][:-1] + myList["suff"][2]} {myList["mm"][2]} {myList[hh + 1][0]}""")
        exit()
    if mm == 59:
        print(f"""{myList[0][2]} {myList[60 - mm][2]} {myList["mm"][1]} {myList[hh + 1][0]}""")
        exit()
    if mm >= 45:
        print(f"""{myList[0][2]} {myList[60-mm][2]} {myList["mm"][2]} {myList[hh + 1][0]}""")
        exit()
