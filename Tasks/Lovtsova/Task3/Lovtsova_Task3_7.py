#7. Write a program that takes a string as input and returns the string with all capital letters converted to lowercase and vice versa.


your_str = input("Please, input your string\n")

print(your_str.swapcase())

# Или:

res=""
for i in your_str:
    if i.isupper():
        res+=i.lower()
    elif i.islower():
        res+=i.upper()
    else:
        res=res+i
print(res)


