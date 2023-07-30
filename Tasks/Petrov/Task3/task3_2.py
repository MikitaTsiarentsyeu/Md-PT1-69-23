while True:
    try:
        numbers = [int(i) for i in input("Enter your numbers: ").split()]
        break
    except ValueError:
        print("Input only integer numbers with a space between them")
        continue

sum = 0
for digit in numbers:
    if digit % 2 == 0:
        sum += digit

print(f"Sum of all even numbers in your input is {sum}")
