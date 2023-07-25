list = list(map(int,input("Enter the numbers using comma:\n").split(",")))

sum = 0
for i in list:
    sum = sum + i
final = sum / len(list)
print(f"The average of all numbers in the list - {final}")



