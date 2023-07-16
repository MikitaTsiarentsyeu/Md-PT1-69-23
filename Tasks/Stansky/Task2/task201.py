from num2words import num2words

time = input('Please, input the time in the format hh:mm and you will get a text representation in Russian:\n')

if len(time) != 5:
    print('Your input is incorrect')
    exit()

hour = time[0:2]
minute = time[3:5]

if not hour.isdigit() or not minute.isdigit():
    print('Your input is incorrect')
    exit()

hour = int(hour)
minute = int(minute)

if 23 < hour or 60 < minute:
    print('Your input is incorrect')
    exit()

dictime = {0: "первого", 1: "второго", 2: "третьего", 3: "четвертого", 4: "пятого",
        5: "шестого", 6: "седьмого", 7: "восьмого",  8: "девятого", 9: "десятого", 10: "одиннадцатого",
        11: "двенадцатого", 12: "первого", 45: "пятнадцати", 46: "четырнадцати",
        47: "тринадцати", 48: "двенадцати", 49: "одиннадцати", 50: "десяти", 51: "девяти",
        52: "восьми", 53: "семи", 54: "шести", 55: "пяти", 56: "четырех", 57: "трех",
        58: "двух", 59: "одной", 101: "одна минута", 102: "две минуты", 121: "двадцать одна минута",
        122: "двадцать две минуты", 131: "тридцать одна минута", 132: "тридцать две минуты",
        141: "сорок одна минута", 142: "сорок две минуты"}

if minute == 0 and (hour == 1 or hour == 13):
    print('один час ровно')
    exit()
elif minute == 0 and (hour == 2 or hour == 3 or hour == 4):
    print(num2words(hour, lang='rus') + ' часа ровно')
    exit()
elif minute == 0 and (hour == 14 or hour == 15 or hour == 16):
    hour = hour - 12
    print(num2words(hour, lang='rus') + ' часа ровно')
    exit()
elif minute == 0 and hour < 13:
    print(num2words(hour, lang='rus') + ' часов ровно')
    exit()
elif minute == 0 and hour > 12:
    hour = hour - 12
    print(num2words(hour, lang='rus') + ' часов ровно')
    exit()

if minute == 30 and hour < 13:
    print('половина ' + dictime[hour])
    exit()
elif minute == 30 and hour > 12:
    hour = hour - 12
    print('половина ' + dictime[hour])
    exit()
if minute == 59 and (hour == 0 or hour == 12):
    print('без ' + dictime[minute] + " минуты " + 'час')
    exit()
elif minute == 59 and (hour == 0 or hour == 12):
    print('без ' + dictime[minute] + " минуты " + 'час')
    exit()
elif minute == 59 and (hour == 0 or hour == 12):
    print('без ' + dictime[minute] + " минуты " + 'час')
    exit()
elif minute >= 45 and (hour == 0 or hour == 12):
    print('без ' + dictime[minute] + " минут " + 'час')
    exit()
elif minute >= 45 and hour < 13:
    print('без ' + dictime[minute] + " минут " + num2words(hour + 1, lang='rus'))
    exit()
elif minute >= 45 and hour > 12:
    hour = hour - 12
    print('без ' + dictime[minute] + " минут " + num2words(hour + 1, lang='rus'))
    exit()
if (minute == 1 or minute == 2 or minute == 21 or minute == 22 or minute == 31
or minute == 32 or minute == 41 or minute == 42) and hour < 13:
    print(dictime[minute+100] + ' ' + dictime[hour])
    exit()
elif (minute == 1 or minute == 2 or minute == 21 or minute == 22 or minute == 31
or minute == 32 or minute == 41 or minute == 42) and hour > 12:
    hour = hour-12
    print(dictime[minute+100] + ' ' + dictime[hour])
    exit()
elif (minute == 3 or minute == 4 or minute == 23 or minute == 24 or minute == 33 or
minute == 34 or minute == 43 or minute == 44) and hour < 13:
    print(num2words(minute, lang='rus') + ' минуты ' + dictime[hour])
    exit()
elif (minute == 3 or minute == 4 or minute == 23 or minute == 24 or minute == 33 or
minute == 34 or minute == 43 or minute == 44) and hour > 12:
    hour = hour - 12
    print(num2words(minute, lang ='rus') + ' минуты ' + dictime[hour])
    exit()
elif minute < 45 and hour < 13:
    print(num2words(minute, lang='rus') + ' минут ' + dictime[hour])
    exit()
elif minute < 45 and hour > 12:
    hour = hour - 12
    print(num2words(minute, lang='rus') + ' минут ' + dictime[hour])
    exit()
    











