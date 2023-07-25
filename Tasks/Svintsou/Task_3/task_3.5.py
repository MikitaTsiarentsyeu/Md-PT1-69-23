x = input('Введите список строк через пробел\n')
x = x.split(' ')
count = []

for i in x:
    if len(i) > 5:
        count.append(i)
if not count:
    print('Все строки меньше 5 символов')
else:
    print(count)