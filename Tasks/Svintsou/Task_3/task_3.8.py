c = input("Введите ваши числа через пробел:\n").split()
sum = 0
x = 0
for i in c:
    sum = sum + int(i)
    x += 1
average = sum / x
print(average)
