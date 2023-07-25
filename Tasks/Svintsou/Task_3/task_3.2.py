x = input("Введите список чисел через пробел: ").split()
even_sum = 0
for i in x:
    if int(i) % 2 == 0:
        even_sum += int(i)
print("Сумма всех четных чисел в списке :", even_sum)