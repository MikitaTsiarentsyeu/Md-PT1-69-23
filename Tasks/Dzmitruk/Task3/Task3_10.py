# a program that takes a list of numbers as input and returns
# the largest primenumber in the list.

n = []

l = input("Please, input a list of numbers: ")

l = list(l.split(", "))

for number in l:
    number = int(number)

    for i in range(1, number):
        i += 1
        if number % i != 0:
            continue

        elif number % i == 0:
            continue

        break
    n.append(number)
    n = sorted(n)
    
print (n[-1], "is the largest prime inumber in the list." )

    

