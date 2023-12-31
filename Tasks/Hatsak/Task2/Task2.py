db = {1: (('один час', 'первого'), 'одна'), 2: (('два часа', 'второго'), 'две'),
      3: (('три часа', 'третьего'), 'три'), 4: (('четыре часа', 'четвёртого'), 'четыре'),
      5: (('пять часов', 'пятого'), 'пять'), 6: (('шесть часов', 'шестого'), 'шесть'),
      7: (('семь часов', 'седьмого'), 'семь'), 8: (('восемь часов', 'восьмого'), 'восемь'),
      9: (('девять часов', 'девятого'), 'девять'), 10: (('десять часов', 'десятого'), 'десять'),
      11: (('одиннадцать часов', 'одиннадцатого'), 'одиннадцать'), 0: (('двенадцать часов', 'двенадцатого'), 'двенадцать'),
      12: (('двенадцать часов', 'двенадцатого'), 'двенадцать'),
      13: ('тринадцать',), 14: ('четырнадцать',), 15: ('пятнадцать',), 16: ('шестнадцать',), 17: ('семнадцать',),
      18: ('восемнадцать',), 19: ('девятнадцать',), 20: ('двадцать',), 30: ('тридцать',), 40: ('сорок',)}
db2 = {1: 'одной минуты', 2: 'двух минут', 3: 'трёх минут', 4: 'четырёх минут', 5: 'пяти минут', 6: 'шести минут',
       7: 'семи минут', 8: 'восьми минут', 9: 'девяти минут', 10: 'десяти минут', 11: 'одиннадцати минут',
       12: 'двенадцати минут', 13: 'тринадцати минут', 14: 'четырнадцати минут', 15: 'пятнадцати минут'}



def enter():
    ent = input("Введите время в формате 'hh:mm': ")
    if len(ent) == 5 and ent[0:2].isdigit() and ent[-2:].isdigit() and 0 <= int(ent[0:2]) < 24 and 0 <= int(ent[-2:]) < 60:
        return (ent[0:2], ent[-2:])
    elif ent.lower() in ('q', 'й'):
        exit()
    else:
        print('Вы можете покинуть программу напечатав "Q"')
        return enter()

while True:

    hh, mm = enter()
    ans_str = ''

    if mm == '00':
        hh = int(hh) % 12
        print(db[hh][0][0].capitalize(), 'ровно')

    elif mm == '30':
        hh = (int(hh)+1) % 12
        print('Половина ', db[hh][0][1])

    elif int(mm) < 45:
        if int(mm) >= 20:
            ans_str = ans_str + db[int(mm[0] + '0')][-1]
            if int(mm) not in (20, 40):
                ans_str = ans_str + ' ' + db[int(mm[-1])][-1]
        else:
            ans_str = ans_str + db[int(mm)][-1]
        if mm in ('01', '21', '31', '41'):
            ans_str = ans_str + ' минута'
        elif int(mm) in (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44):
            ans_str = ans_str + ' минуты'
        else:
            ans_str = ans_str + ' минут'
        hh = (int(hh) + 1) % 12
        ans_str = ans_str + ' ' + db[hh][0][-1]
        print('Ваше время: ', ans_str.capitalize())
    else:
        hh = (int(hh) + 1) % 12
        ans_str = 'Без ' + db2[60 - int(mm)] + ' '
        if hh not in (1, 2):
            ans_str = ans_str + db[hh][-1]
        elif hh == 1:
            ans_str = ans_str + 'час'
        else:
            ans_str = ans_str + 'два'
        print('Ваше время: ', ans_str.capitalize())



