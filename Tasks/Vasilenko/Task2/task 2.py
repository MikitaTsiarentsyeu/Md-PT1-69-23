print("Here you can find out how the time is interpreted in Russian")

user_time = input("Please, enter the time (hh:mm):\n")

if len(user_time) != 5 and user_time[2] != ':':
    print ("Your input is incorrect. Please, enter the time in the right format.")
    exit()

hhmm = user_time.split(":")
hh = hhmm[0]
mm = hhmm[1]

if not hh.isdigit() or not mm.isdigit():
    print("Your input is incorrect. Please, enter the time in the right format.")
    exit()

hh, mm = int(hh), int(mm)

if hh > 23 or mm > 59:
    print("Your input is incorrect. Please, enter the time in the right format.")
    exit()

tup_hours = ('час', 'часа', 'часов')
tup_minutes = ('минута', 'минуты', 'минут')

tup_hh_nom = ('один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать')
tup_hh_gen = ('первого', 'второго', 'третьего', 'четвертого', 'пятого', 'шестого', 'седьмого', 'восьмого', 'девятого', 'десятого', 'одиннадцатого', 'двенадцатого')

l_hh_nom = list(tup_hh_nom)
l_mm_nom = ['одна', 'две'] + l_hh_nom[2:] + ['тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
tup_mm_nom = tuple(l_mm_nom)

tup_mm_doz = ('двадцать', 'тридцать', 'сорок')
tup_mm_gen = ('одной', 'двух', 'трех', 'четырех', 'пяти', 'шести', 'семи', 'восьми', 'девяти', 'десяти', 'одиннадцати', 'двенадцати', 'тринадцати', 'четырнадцати', 'пятнадцати')


if hh > 11:
    hh = hh - 12

dict_hh = {0:tup_hh_nom[-1], 1:tup_hh_nom[0], 2:tup_hh_nom[1], 3:tup_hh_nom[2], 4:tup_hh_nom[3], 5:tup_hh_nom[4], 6:tup_hh_nom[5], 7:tup_hh_nom[6], 8:tup_hh_nom[7], 9:tup_hh_nom[8], 10:tup_hh_nom[9], 11:tup_hh_nom[10]}
dict_mm = {1:tup_mm_nom[0], 2:tup_mm_nom[1], 3:tup_mm_nom[2], 4:tup_mm_nom[3], 5:tup_mm_nom[4], 6:tup_mm_nom[5], 7:tup_mm_nom[6], 8:tup_mm_nom[7], 9:tup_mm_nom[8], 10:tup_mm_nom[9], 11:tup_mm_nom[10], 12:tup_mm_nom[11], 13:tup_mm_nom[12], 14:tup_mm_nom[13], 15:tup_mm_nom[14], 16:tup_mm_nom[15], 17:tup_mm_nom[16], 18:tup_mm_nom[17], 19:tup_mm_nom[18]}

if hh == 1:
    hours = tup_hours[0]
elif hh > 1 and hh < 5:
    hours = tup_hours[1]
else:
    hours = tup_hours[2]


if 0 < mm < 10 or 20 < mm < 45:
    if (mm-1)%10 == 0:
        minutes = tup_minutes[0]
    elif (mm-2)%10 == 0 or (mm-3)%10 == 0 or (mm-4)%10 == 0:
        minutes = tup_minutes[1]
    else:
        minutes = tup_minutes[2]
        mm = int(mm)
elif mm == 59:
    minutes = tup_minutes[1]
else:
    minutes = tup_minutes[2]


if mm == 0:
    print(f'{dict_hh[hh]} {hours} ровно')
elif mm > 0 and mm < 20:
    print(f'{dict_mm[mm]} {minutes} {tup_hh_gen[hh]}')
elif mm >= 20 and mm < 30:
    print(f'{tup_mm_doz[0]} {dict_mm[mm-20]} {minutes} {tup_hh_gen[hh]}')
elif mm == 30:
    print(f'половина {tup_hh_gen[hh]}')
elif mm > 30 and mm < 40:
    print(f'{tup_mm_doz[1]} {dict_mm[mm-30]} {minutes} {tup_hh_gen[hh]}')
elif mm >= 40 and mm < 45:
    print(f'{tup_mm_doz[2]} {dict_mm[mm-40]} {minutes} {tup_hh_gen[hh]}')
elif mm >= 45:
    if hh == 0:
        l_hh_nom = list(tup_hh_nom)
        l_hh_nom[0] = 'час'
        tup_hh_nom = tuple(l_hh_nom)
    print(f'без {tup_mm_gen[59-mm]} {minutes} {tup_hh_nom[hh]}')
