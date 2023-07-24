"""10. Write a program that takes a list of numbers as input and returns the largest prime number in the list."""
from list_input import enter

nums = enter()


def is_prime(num):
    if num == 1:
        return False
    l = 2
    r = int(num/2) + 1
    for div in range(l, r):
        if num % div == 0:
            return False
    else:
        return True


nums.sort(reverse=True)
for num in nums:
    if is_prime(num):
        print(num)
        break
else:
    print('No prime numbers in a list!')
