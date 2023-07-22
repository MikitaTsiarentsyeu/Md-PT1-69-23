numbers = (input('Please, input a list of integers in format "n,n,n":\n'))
numbers = numbers.split(',')

total = 0

for i in numbers:
    try:
        i = int(i)
        if i % 2 == 0:
            total += i

    except:
        print("Your input is incorrect")
        exit()

print(f'The sum of all even numbers in the list: {total}')









