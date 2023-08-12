"""Write a recursive function to find the Nth number in the Fibonacci sequence"""

input_number = input('Please, enter the sequence number of the Fibonacci sequence you want to find:\n')


def fibonacci_number(number, number1=0, number2=1):
    if number == 1:
        return number1
    elif number == 2:
        return number2
    else:
        return fibonacci_number(number-1, number1=number2, number2=number1+number2)


print(f'The number you want to find is {fibonacci_number(int(input_number))}')
