from decimal import Decimal, InvalidOperation

while True:
    try:
        numbers = [Decimal(i) for i in input("Enter your numbers: ").split()]
        break
    except InvalidOperation:
        print("Input only numbers with a space between them")
        continue

if len(numbers) <= 1:
    print("There is no two numbers in your input")
    exit()
largest = numbers[0]
second_largest = numbers[1]
for digit in numbers:
    if digit > largest:
        largest, second_largest = digit, largest
        continue
    if digit > second_largest and digit != largest:
        second_largest = digit

print(f"The second largest number in your input is {second_largest}")
