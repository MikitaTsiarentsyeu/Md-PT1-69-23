list = list(map(int,input("Enter the list of numbers using comma:\n").split(",")))

zero = 0

for i in list:
    if i % 2 == 0:
        zero = zero + i
print(f"The sum of all even numbers in the list - {zero}")