def primes(num):
    if num <= 1:
        return []
    primes = [2]
    for digit in range(3, num + 1, 2):
        isprime = True
        for prime in primes:
            if prime > int(digit ** 0.5) + 2:
                break
            if digit % prime == 0:
                isprime = False
                break
        if isprime:
            primes.append(digit)
    return primes


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
primes_list = primes(numbers[0])
isnotfound = True
for number in numbers:
    if number in primes_list:
        print(f"The largest prime number in your input is {number}")
        isnotfound = False
        break
if isnotfound:
    print("No prime numbers in your input")
