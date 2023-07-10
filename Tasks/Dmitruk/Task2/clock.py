# Implement a text output of the time entered from the console 

dict_clock = { 0 : [ "ноль" ], 1 : [ "один", "первого", "одной" ], 2 : [ "два", "второго", "двух" ],
               3 : [ "три", "третьего", "трех"],4 : [ "четыре", "четвертого", "четырех" ],
               5 : ["пять", "пятого", "пяти" ], 6 : [ "шесть", "шестого", "шести" ],
               7 : [ "семь", "седьмого", "семи" ], 8 : [ "восемь", "восьмого", "восьми" ],
               9 : [ "девять", "девятого", "девяти" ], 10 : [ "десять", "десятого", "десяти" ],
               11 : [ "одиннадцать", "одиннадцатого", "одиннадцати" ], 12 : [ "двенадцать", "двенадцатого", "двенадцати" ],
               13 : [ "триадцать", "час", "тринадцати" ], 14 : [ "четырнадцать", "второго", "четырнадцати" ],
               15 : [ "пятнадцать", "третьего", "пятнадцати" ], 16 : [ "шестнадцать" ], 17 : [ "семнадцать" ],
               18 : [ "восемнадцать" ], 19 : [ "девятнадцать" ], 20 : ["двадцать" ], 21 : [ "двадцать одна" ],
               22 : [ "двадцать две" ],  23 : [ "двадцать три" ], 24 : [ "двадцать четыре" ], 25 :  [ "двадцать пять" ],
               26 : [ "двадцать шесть" ], 27 : [ "двадцать семь" ], 28 : [ "двадцать восемь" ], 29 : [ "двадцать девять" ],
               31 : [ "тридцать одна" ], 32 : [ "тридцать две" ], 33 : [ "тридцать три" ], 34 : [ "тридцать четыре" ],
               35 : [ "тридцать пять" ],  36 : [ "тридцать шесть" ], 37 : [ "тридцать семь" ], 38 : [ "тридцать восемь" ],
               39 : [ "тридцать девять" ], 40 : [ "сорок" ], 41 : [ "сорок одна" ], 42 : [ "сорок две" ], 
               43 : [ "сорок три" ], 44 : [ "сорок четыре" ] }


time = input ( "Pleese input time in format (hh:mm): \n" )

new_time = time.replace (":", "")

if not new_time.isdigit():

    print ("Your enter a wrong time.")
    exit()

hours, minutes = time.split (":")
hours = int (hours)
minutes = int (minutes)

if  hours < 0 or hours > 24:

    print ("Your enter a wrong time.")
    exit()

if  minutes < 0 or minutes > 59:

    print ("Your enter a wrong time.")
    exit()

if minutes == 0:

    if hours > 12:

        hours -= 12

    if hours == 1:

        print ( dict_clock [hours][0], "час ровно" )

    elif 1 <  hours <= 4:

        print ( dict_clock [hours][0], "часa ровно" )

    else:

        print ( dict_clock [hours][0], "часов ровно" )

elif minutes == 30:

    print ( "половина", dict_clock [hours + 1][1] )

elif 0 < minutes < 30 or 30 < minutes < 45:

    if hours >= 12:

        hours -= 12

    if minutes in [ 21, 31, 41 ]:

        print ( dict_clock [minutes][0], "минутa", dict_clock [hours + 1][1] )

    elif minutes in [ 22, 23, 24, 32, 33, 34, 42, 43, 44 ]:

        print ( dict_clock [minutes][0], "минуты", dict_clock [hours + 1][1] )

    else:
        print ( dict_clock [minutes][0], "минут", dict_clock [hours + 1][1] )

elif minutes >= 45:

    minutes = 60 - minutes

    if hours == 0:

        hours += 12

        print ( "без", dict_clock [minutes][2], "минут", dict_clock [hours + 1][1] )

    if hours > 12:

        hours -= 12

        print ( "без", dict_clock [minutes][2], "минут", dict_clock [hours + 1][0] )

    else:

        print ( "без", dict_clock [minutes][2], "минут", dict_clock [hours + 1][1] )
        