import math
import random

while True:
    print("Выберите программу:")
    print("1 - Конвертер температуры")
    print("2 - Вычисление площади окружности")
    print("3 - Конвертер скорости")
    print("4 - Конвертер валют")
    print("5 - Генератор случайных чисел")

        speed_ms = speed_kmh * 1000 / 3600
    choice = input()
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            celsius = float(input("Введите температуру в градусах Цельсия: "))
            fahrenheit = (celsius * 1.8) + 32
            print(f"Температура по Фаренгейту: {fahrenheit:.2f}")
        elif choice == 2:
            radius = float(input("Введите радиус окружности: "))
            area = math.pi * radius ** 2
            print(f"Площадь окружности: {area:.2f}")
        elif choice == 3:
            speed_kmh = float(input("Введите скорость в километрах в час: "))
            speed_ms = speed_kmh * 1000 / 3600
            print(f"Скорость в метрах в секунду: {speed_ms:.2f}")
        elif choice == 4:
            usd_to_byn = 3
            usd_amount = float(input("Введите сумму в USD: "))
            byn_amount = usd_amount * usd_to_byn
            print(f"Сумма в BYN: {byn_amount:.2f}")
        elif choice == 5:
            left = int(input("Введите левую границу: "))
            right = int(input("Введите правую границу: "))
            while left >= right:
                print("Левая граница должна быть меньше правой границы!")
                left = int(input("Введите левую границу: "))
                right = int(input("Введите правую границу: "))
            random_number = random.randint(left, right)
            print(f"Случайное число в диапазоне от {left} до {right}: {random_number}")
        else:
            print("Некорректный выбор.")
    else:
        print("Некорректный выбор.")

    # Запросить у пользователя продолжение работы
    again = input("Хотите продолжить работу? (y/n): ")
    if again.lower() != "y":
        break
