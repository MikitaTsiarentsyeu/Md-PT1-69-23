
def num_fibonacci(number):
    """ a recursive function to find the Nth number in the Fibonacci sequence """

    if number == 1:
        return 0
    if number == 2:
        return 1
    fibonacci = num_fibonacci(number - 1) + num_fibonacci(number - 2)
    return fibonacci