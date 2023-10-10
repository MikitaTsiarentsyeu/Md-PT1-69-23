values = {
    1:("час", "первого", "одна", "одной"),
    2:("два", "второго", "две", "двух"),
    3:("три", "третьего", "три", "трех"),
    4:("четыре", "четвертого", "четыре", "четырех"),
    5:("пять", "пятого", "пять", "пяти"),
    6:("шесть", "шестого", "шесть", "шести"),
    7:("семь", "седьмого", "семь", "семи"),
    8:("восемь", "восьмого", "восемь", "восьми"),
    9:("девять", "девятого", "девять", "девяти"),
    10:("десять", "десятого", "десять", "десяти"),
    11:("одиннадцать", "одиннадцатого", "одиннадцать", "одиннадцати"),
    12:("двенадцать", "двенадцатого", "двенадцать", "двенадцати"),
    13:("", "", "тринадцать", "тринадцати"),
    14: ("", "", "четырнадцать", "четырнадцати"),
    15: ("", "", "пятнадцать", "пятнадцати"),
    16: ("", "", "шестнадцать", "шестнадцати"),
    17: ("", "", "семнадцать", "семнадцати"),
    18: ("", "", "восемнадцать", "восемнадцати"),
    19: ("", "", "девятнадцать", "девятнадцати"),
    20: ("", "", "двадцать", "двадцати"),
    30: ("", "", "тридцать", "тридцати"),
    40: ("", "", "сорок", "сорока")
}

minute_part_No2 = 0
user_time = input("Write time there trough ':' in hh:mm format :")

user_time_list = user_time.split(":")

hours = user_time_list[0]
minutes = user_time_list[1]

while hours.isdigit() == False or minutes.isdigit() == False:
    print("Write time there trough ':' in hh:mm format :")

hours_list = hours.split()
if hours_list[0] == '0':
    hours = int(hours_list[1])
else:
    hours = int(hours)

minutes_list = minutes.split()
if minutes_list[0] == '0' and minutes_list[1] == '0':
    minutes = 0
elif minutes_list[0] == '0' and minutes_list[1] != '0':
    minutes = int(minutes_list[1])
else:
    minutes = int(minutes)

if minutes > 0:
    hours += 1

if hours > 12:
    hours = hours - 12

if minutes > 20 and minutes < 30 or minutes > 30 and minutes < 45:
    minutes = str(minutes)
    minute_part_No1 = minutes[0] + '0'
    minute_part_No2 = minutes[1]
    minute_part_No1, minute_part_No2 = int(minute_part_No1), int(minute_part_No2)
    minutes = int(minutes)

if minutes == 0 and hours == 1:
    res_hours = values.get(hours)
    print(res_hours[0], 'ровно')

elif minutes == 0 and hours != 1 and hours < 5:
    res_hours = values.get(hours)
    print(res_hours[0], 'часа ровно')

elif minutes == 0 and hours != 1 and hours >= 5:
    res_hours = values.get(hours)
    print(res_hours[0], 'часов ровно')

elif minutes > 0 and minutes <= 20:
    res_hours = values.get(hours)
    res_minutes = values.get(minutes)
    print(res_minutes[0], 'минут', res_hours[1])

elif minute_part_No2 == 1:
    res_hours = values.get(hours)
    res_minutes_part_No1 = values.get(minute_part_No1)
    res_minutes_part_No2 = values.get(minute_part_No2)
    print(res_minutes_part_No1[2], res_minutes_part_No2[2], 'минутa', res_hours[1])

elif minutes > 21 and minutes < 25 or minutes > 31 and minutes < 35 or minutes > 41 and minutes < 45:
    res_hours = values.get(hours)
    res_minutes_part_No1 = values.get(minute_part_No1)
    res_minutes_part_No2 = values.get(minute_part_No2)
    print(res_minutes_part_No1[2], res_minutes_part_No2[2], 'минуты', res_hours[1])

elif minutes >= 25 and minutes < 30 or minutes >= 35 and minutes < 40:
    res_hours = values.get(hours)
    res_minutes_part_No1 = values.get(minute_part_No1)
    res_minutes_part_No2 = values.get(minute_part_No2)
    print(res_minutes_part_No1[2], res_minutes_part_No2[2], 'минут', res_hours[1])

elif minutes == 30:
    res_hours = values.get(hours)
    print('половина', res_hours[1])

elif minutes >= 45:
    minutes = 60 - minutes
    res_hours = values.get(hours)
    res_minutes = values.get(minutes)
    if minutes == 1:
        print('без', res_minutes[3], 'минуты', res_hours[0])
    else:
        print('без', res_minutes[3], 'минут', res_hours[0])
