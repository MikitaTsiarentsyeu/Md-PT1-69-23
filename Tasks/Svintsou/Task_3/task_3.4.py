def second_largest(numbers):
    numbers = list(set(numbers))  
    numbers.sort()  
    return numbers[-2]  # Возвращаем второе максимальное число (второе с конца)

user_input = list(map(int, input("Введите ваши числа через пробел: ").split()))
print("Второе по величине число в списке:", second_largest(user_input))
