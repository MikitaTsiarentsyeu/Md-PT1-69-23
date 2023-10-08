#10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.


list_inp=[5,7,10,11,22,43,5,7,10,11,22,43]
#list_inp=[10,22,16]

largest_prime_number=0
for i in list_inp:
    h=0
    k=1
    while k<=i:
        if i%k==0:
            h=h+1
        k+=1

    if h==2 and largest_prime_number<i:
        largest_prime_number=i

if largest_prime_number==0:
    print("none prime number")
else:
    print(largest_prime_number)
