#2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

list_1=[5,7,10,11,22,43,5,7,10,11,22,43]
#list_1=[1,2,3,4,5,6,7,8,9,10]
#list_1=[345,234,2.07,45,-34,23.78,99,-3]
sum=0
for i in list_1:
    if i % 2 == 0:
        sum = sum+i
print(sum)