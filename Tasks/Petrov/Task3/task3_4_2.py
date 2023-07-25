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
largest = max(numbers)
while largest in numbers:
    numbers.remove(largest)
largest = max(numbers)

print(f"The second largest number in your input is {largest}")
