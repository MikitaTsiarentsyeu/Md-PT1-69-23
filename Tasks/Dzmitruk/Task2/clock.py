# Implement a text output of the time entered from the console 

clock = { 1 : [ "час", "одной", "первого", "одна" ],
          2 : [ "два", "двух", "второго", "две" ],
          3 : [ "три", "трех", "третьего", "три" ],
          4 : [ "четыре", "четырех", "четвертого", "четыре" ],
          5 : ["пять", "пяти", "пятого", "пять" ],
          6 : [ "шесть", "шести", "шестого", "шесть" ],
          7 : [ "семь", "семи", "седьмого", "семь" ],
          8 : [ "восемь", "восьми", "восьмого", "восемь" ],
          9 : [ "девять", "девяти", "девятого", "девять" ],
          10 : [ "десять", "десяти", "десятого" ],
          11 : [ "одиннадцать", "одиннадцати", "одиннадцатого" ],
          12 : [ "двенадцать", "двенадцати", "двенадцатого" ],
          13 : [ "триадцать", "тринадцати" ],
          14 : [ "четырнадцать","четырнадцати" ],
          15 : [ "пятнадцать", "пятнадцати" ],
          20 : ["двадцать" ], 30 : [ "тридцать" ], 40 : [ "сорок" ] }


time = input ( "Pleese input the time in the format (hh:mm): \n" )

if not time.count(":"):
    print ("Your entered the wrong time.")
    exit()

new_time = time.replace (":", "")

if not new_time.isdigit():
    print ("Your entered the wrong time.")
    exit()
    
try:
    hours, minutes = time.split (":")
    
    if len(minutes) != 2:
        print ("Your entered the wrong time.")
        exit()
    
    hours = int (hours)
    minutes = int (minutes)

except ValueError as msg:
    print ("Need more than 1 value.")
    exit()

if  hours < 0 or hours > 24:
    print ("Your entered the wrong time.")
    exit()

if  minutes < 0 or minutes > 59:
    print ("Your entered the wrong time.")
    exit()

if minutes == 0:
    if hours > 12:
        hours -= 12

    if hours == 0:
        hours += 12
        
    if hours == 1:
        print ( "один", clock [hours][0], "ровно" )

    elif 1 <  hours <= 4:
        print ( clock [hours][0], "часa ровно" )

    else:
        print ( clock [hours][0], "часов ровно" )

elif minutes == 30:
    if hours >= 12:
        hours -= 12
    print ( "половина", clock [hours + 1][2] )

elif 0 < minutes < 30 or 30 < minutes < 45:
    if hours >= 12:
        hours -= 12

    if minutes == 1:
        print ( clock [minutes][3], "минутa", clock [hours + 1][2] )

    elif minutes in [ 2, 3, 4 ]:
        print ( clock [minutes][3], "минуты", clock [hours + 1][2] )

    elif minutes % 10 != 0 and minutes > 15:
        digit_1 = minutes // 10
        digit_2 = minutes % 10
        
        if digit_2 == 1:
            print ( clock [digit_1 * 10][0], clock [digit_2][3], "минутa", clock [hours + 1][2] )

        elif digit_2 in [ 2, 3, 4 ]:
            print ( clock [digit_1 * 10][0], clock [digit_2][3], "минуты", clock [hours + 1][2] )

        else:
            print ( clock [digit_1 * 10][0], clock [digit_2][3], "минут", clock [hours + 1][2] )

    else:
        print ( clock [minutes][0], "минут", clock [hours + 1][2] )

elif minutes >= 45:
    minutes = 60 - minutes

    if hours >= 12:
        hours -= 12
        print ( "без", clock [minutes][1], "минут", clock [hours + 1][0] )
     
    else:
        print ( "без", clock [minutes][1], "минут", clock [hours + 1][0] )
