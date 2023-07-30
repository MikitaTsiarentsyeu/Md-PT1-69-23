def isprime(num):
    check_number = 3
    while check_number ** 2 <= num:
        if num % check_number == 0:
            return False
        check_number += 2
    return True


while True:
    try:
        numbers = [int(i) for i in input("Enter your numbers: ").split()]
        if len(numbers) == 0:
            print("No numbers")
            exit()
        break
    except ValueError:
        print("Input only integer numbers with a space between them")
        continue

numbers = list(reversed(sorted(numbers)))
if numbers[0] <= 1:
    print("No prime numbers in your input")
    exit()
elif numbers[0] == 2:
    print("The largest prime number in your input is 2")
    exit()
for number in numbers:
    if isprime(number):
        print(f"The largest prime number in your input is {number}")
        break
