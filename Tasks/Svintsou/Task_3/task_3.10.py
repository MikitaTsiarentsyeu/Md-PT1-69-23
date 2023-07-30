def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        
    return True

print("Введите список через пробел:")
number = list(map(int, input().split()))

max = 0

for i in number:
    if is_prime(i) and i > max:
        max = i

if (max == 0):
    print("Простых чисел в вашем списке нет")
else:
    print("Наибольшее простое число в вашем списке:", max)