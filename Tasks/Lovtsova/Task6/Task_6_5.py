def fibonacci_n (n_th:int) ->int:
    """5. The recursive function to find 
    the Nth number in the Fibonacci sequence"""
    if n_th==0:
        return 1
    elif n_th==1:
        return 2
    else:
        return fibonacci_n(n_th-1)+fibonacci_n(n_th-2)

while True:
    try:
        n_th=int(input("Please, enter your integer to calcutate the Fibonacci number:\n"))
        break
    except ValueError:    
        print ("\t\t Please, try again!")
        continue

print(f'\t For {n_th} the Fibonacci number is {fibonacci_n(n_th)}\n')