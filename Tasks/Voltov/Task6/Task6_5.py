# 5. Write a recursive function to find the Nth number in the Fibonacci sequence.
# 0, 1, 2, 3, 5, 8, 13, 21, ...
def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter the number of terms in the sequence:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))