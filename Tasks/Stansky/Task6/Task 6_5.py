n = input('Please, input the element number in the Fibonacci sequence:\n')
try:
    n = int(n)
except:
    print('Incorrect. Input а positive integer!')
    exit()

if n >= 1:
    pass
else:
    print('Incorrect. Input а positive integer!')
    exit()

def number_fibonacci(n):
    if n == 1:
        return 0
    number = 1
    if n > 3:
        number = number_fibonacci(n-1) + number_fibonacci(n-2)
    return number


print(f'At position {n} in the Fibonacci sequence is the number {number_fibonacci(n)}')