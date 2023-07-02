import random

left = int(input("Введите левую границу: "))

right = int(input("Введите правую границу: "))


random_number = random.randint(left, right)

print(f"Случайное число в диапазоне от {left} до {right}: {random_number}")




