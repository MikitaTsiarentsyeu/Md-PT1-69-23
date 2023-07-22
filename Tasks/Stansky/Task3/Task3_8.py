numbers = input('Please, input a list of numbers in format: "N, N, N":\n')
numbers = numbers.split(',')
nums = 0
try:
    for s in numbers:
        s = float(s)
        nums += s
except:
    print('Your input is incorrect')
    exit()

aver = nums/len(numbers)

print(f'Average of all numbers in the list is: {aver}')

