# a program that takes a list of numbers as input and returns
# the largest primenumber in the list.

prime_numbers = []

l = input("Please, input a list of numbers: ")

l = list(l.split(", "))

for num in l:
    num = int(num)
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_numbers.append(num)

prime_numbers = sorted(prime_numbers)
   
print (prime_numbers[-1], "is the largest prime number in the list." )

    

