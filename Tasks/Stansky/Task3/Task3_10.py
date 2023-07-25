numbers = input('Please, input a list of integers  in format "n, n, n":\n ')
numbers = numbers.split(',')
values = []
numbers_prime = []
try:
    for n in numbers:
        n = int(n)
        values.append(n)
except:
    print('Your input is incorrect')
    exit()

for s in values:
    if s > 1:
        for k in range(2, s):
            if s % k == 0:
                break
        else:
            numbers_prime.append(s)

print(f'The largest prime number in the list is:  {max(numbers_prime)}')




