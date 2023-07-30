from decimal import Decimal, InvalidOperation

while True:
    try:
        numbers = [Decimal(i) for i in input("Enter your numbers: ").split()]
        if len(numbers) == 0:
            print("No numbers - no average")
            exit()
        break
    except InvalidOperation:
        print("Input only numbers with a space between them")
        continue

sum = 0
for number in numbers:
    sum += number
print(f"The average is {round(sum / len(numbers), 2)}")
