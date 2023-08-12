def Fibonacci(number):
    if number<= 0:
        print("Incorrect input")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return Fibonacci(number-1)+Fibonacci(number-2)
print(Fibonacci(15))