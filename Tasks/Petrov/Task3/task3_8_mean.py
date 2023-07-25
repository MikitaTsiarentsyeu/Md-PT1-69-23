from decimal import Decimal, InvalidOperation
from statistics import mean

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

print(f"The average is {round(mean(numbers), 2)}")
