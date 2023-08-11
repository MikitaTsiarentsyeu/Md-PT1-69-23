def fibonacci(x, y=0, z=1):
    if x == 1:
        return 0

    if x == 2:
        return 1

    return y + fibonacci(x - 1, z, y + z)


print(fibonacci(7))

