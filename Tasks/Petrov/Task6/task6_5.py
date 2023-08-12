def fibonacci(needed, current=3, number=1, previous=1):
    if needed == current:
        return number
    elif needed not in [1, 2]:
        return fibonacci(needed, current + 1, number + previous, number)
    return 0 if needed == 1 else previous


while True:
    try:
        n = int(input("Enter the position of the number in Fibonacci sequence: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("This should be an integer and positive number")
        continue

print(f"The {n}th number in the Fibonacci sequence is {fibonacci(n)}")
