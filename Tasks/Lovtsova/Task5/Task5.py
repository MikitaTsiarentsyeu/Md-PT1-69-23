#1. Write a function that takes two integers as arguments and returns their sum.

def sum(a,b):
    res = a+b
    return res
print(sum(7,14))
print(sum(sum(1,2),sum(3,4)))

#2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.
def str_ret(str):
    res=(str[::-1])
    return res
print(str_ret('a new list of strings that are all reversed'))

#3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

def greater5(list):
    list_5=[]
    for i in list:
        if len(i)>5:
            list_5.append(i)
    return list_5
print(greater5(['a new','list',' of ','strings','that are all reversed']))

#4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case symbols, second for count of the upper case symbols in the initial string.

def registr(my_str):
    lower=0
    upper=0
    for i in my_str:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
    return(f'lower = {lower}  &  upper = {upper}')
#Считаем раздельно, чтобы исключить пробелы, цифры и другие знаки, в том числе знаки препинания
print(registr('Gjise oHUK,F,klj.@..fb678su;io---ue ouFRJ  UYio.vsHk;gh'))

#5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#get_ranges([4,7,10])  -> "4, 7, 10"
#get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

def get_ranges(my_list):
    res = []
    first=my_list[0]
    last=my_list[0]
    
    for i in range(1,(len(my_list))):
        if my_list[i] == last + 1:
            last = my_list[i]
        else:
            if first != last:
                res.append(f"{first}-{last}")
            else:
                res.append(f"{first}")
            first=last=my_list[i]
    if first != last:
        res.append(f"{first}-{last}")
    else:
        res.append(f"{first}")

    return ', '.join(res)

print(get_ranges([17]))
print(get_ranges([0, 1, 2, 4, 7, 8, 10, 6, 7, 8, 10, 11, 17]))
print(get_ranges([4, 6, 7, 10]))
print(get_ranges([1, 2, 8, 9, 10, 2, 3, 4, 8, 9]))