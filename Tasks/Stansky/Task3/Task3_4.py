numbers = input('Please, input a list of numbers in format"n,n,n" and you will get the second largest number:\n')
numbers = numbers.replace(' ', '')
numbers = numbers.split(',')
numbers = set(numbers)
numbers = list(numbers)

try:
    maximum1 = float(numbers[0])
    maximum2 = float(numbers[0])

    for num1 in numbers:
        num1 = float(num1)
        if num1 > maximum1:
            maximum1 = num1
    if maximum1 == maximum2:
        maximum2 = float(numbers[1])

    for num2 in numbers:
        num2 = float(num2)
        if maximum2 < num2 < maximum1:
            maximum2 = num2

    print(f'The second largest number is {maximum2}')

except:
    print('Your input is incorrect')
    exit()



