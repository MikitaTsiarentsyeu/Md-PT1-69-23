# 10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

numbers = input("Enter a list of numbers separated by a space: ").split()

largest_prime = None
for num in numbers:
    num = int(num)
    if is_prime(num) and (largest_prime is None or num > largest_prime):
        largest_prime = num

if largest_prime is not None:
    print("Largest prime number in the list:", largest_prime)
else:
    print("There are no prime numbers in the list.")