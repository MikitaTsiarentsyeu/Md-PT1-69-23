from time import strptime


# def checktime(possible_time): <----------------------------- works too
#     if len(possible_time) != 5:
#         print("Incorrect input, try again")
#         return False
#     elif possible_time[2] != ":":
#         print("Incorrect input, try again")
#         return False
#     elif not possible_time[0:2].isdigit() or not possible_time[3:].isdigit():
#         print("Incorrect input, try again")
#         return False
#     elif int(possible_time[0:2]) > 23 or int(possible_time[3:]) > 59:
#         print("Incorrect input, try again")
#         return False
#     else:
#         print("Alright")
#         return True


def checktime(possible_time):
    try:
        strptime(possible_time, "%H:%M")
        print("Alright")
        return True
    except ValueError:
        print("Incorrect input, try again")
        return False


while True:
    given_time = input("Input the time in hh:mm format: ")
    if checktime(given_time):
        break

hours_str, minutes_str = given_time.split(":")
hours, minutes = int(hours_str), int(minutes_str)

time_dict = {
    1: ["одна минута", "одной минуты", "один час", "первого"],
    2: ["две минуты", "двух минут", "два часа", "второго"],
    3: ["три минуты", "трёх минут", "три часа", "третьего"],
    4: ["четыре минуты", "четырёх минут", "четыре часа", "четвёртого"],
    5: ["пять минут", "пяти минут", "пять часов", "пятого"],
    6: ["шесть минут", "шести минут", "шесть часов", "шестого"],
    7: ["семь минут", "семи минут", "семь часов", "седьмого"],
    8: ["восемь минут", "восьми минут", "восемь часов", "восьмого"],
    9: ["девять минут", "девяти минут", "девять часов", "девятого"],
    10: ["десять минут", "десяти минут", "десять часов", "десятого"],
    11: ["одиннадцать минут", "одиннадцати минут", "одиннадцать часов", "одиннадцатого"],
    12: ["двенадцать минут", "двенадцати минут", "двенадцать часов", "двенадцатого"],
    13: ["тринадцать минут", "тринадцати минут"],
    14: ["четырнадцать минут", "четырнадцати минут"],
    15: ["пятнадцать минут", "пятнадцати минут"],
    16: ["шестнадцать минут"],
    17: ["семнадцать минут"],
    18: ["восемнадцать минут"],
    19: ["девятнадцать минут"],
    20: ["двадцать минут"],
    21: ["двадцать одна минута"],
    22: ["двадцать две минуты"],
    23: ["двадцать три минуты"],
    24: ["двадцать четыре минуты"],
    25: ["двадцать пять минут"],
    26: ["двадцать шесть минут"],
    27: ["двадцать семь минут"],
    28: ["двадцать восемь минут"],
    29: ["двадцать девять минут"],
    31: ["тридцать одна минута"],
    32: ["тридцать две минуты"],
    33: ["тридцать три минуты"],
    34: ["тридцать четыре минуты"],
    35: ["тридцать пять минут"],
    36: ["тридцать шесть минут"],
    37: ["тридцать семь минут"],
    38: ["тридцать восемь минут"],
    39: ["тридцать девять минут"],
    40: ["сорок минут"],
    41: ["сорок одна минута"],
    42: ["сорок две минуты"],
    43: ["сорок три минуты"],
    44: ["сорок четыре минуты"]
}

hours_12 = hours if hours < 12 else abs(12 - hours)
if minutes == 0:
    print(f"{given_time} - {time_dict[12][2] if hours_12 == 0 else time_dict[hours_12][2]} ровно")
elif minutes < 30:
    print(f"{given_time} - {time_dict[minutes][0]} {time_dict[hours_12+1][3]}")
elif minutes == 30:
    print(f"{given_time} - половина {time_dict[hours_12+1][3]}")
elif 45 > minutes > 30:
    print(f"{given_time} - {time_dict[minutes][0]} {time_dict[hours_12+1][3]}")
else:
    print(f"{given_time} - без {time_dict[60-minutes][1]} {time_dict[hours_12+1][2].split()[1] if hours_12 == 0 else time_dict[hours_12+1][2].split()[0]}")
