#1. Write a function that takes two integers as arguments and returns their sum.
def plus(a,b):
    c = a + b
    return c 
print(plus(10,22))

#2. Write a function that takes a list of strings as an argument 
#and returns a new list of strings that are all reversed.
def revers(list):
    newlist = []
    for words in list:
        newlist.append(words[::-1])
    return newlist
list = ["dog","ball","green","black","window"]
print(revers(list))

#3. Write a function that takes a list of strings as an argument 
#and returns a new list with all the strings that have a length greater than 5.
def lenght (list):
    newlist = []
    for words in list:
        if len(words) > 5:
            newlist.append(words)
    return newlist
list = ["dog","helicopter","comfortable","ball","exchange"]
print(lenght(list))

#4. Write a function that takes a string as an argument and returns two numbers, 
#first for count of lower case symbols, second for count of the upper case symbols in the initial string.
def case(string):
    lowercase = 0
    uppercase = 0
    for symbol in string:
        if symbol == symbol.upper():
            uppercase +=1
        if symbol == symbol.lower():
            lowercase +=1
    result = f"You value for lowercase - {lowercase}\nYou value for uppercase - {uppercase}"
    return result
string = "AcHbasdGGnMuaTTdfdfgdfgYYUAbbDf"
print(case(string))

# 5. Write a function that takes an ordered list of numbers without duplicates 
#and returns a string with ranges for those numbers, check the example below:
#get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#get_ranges([4,7,10])  -> "4, 7, 10"
#get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
def get_ranges(list):
    newlist = []
    firstborder = secondborder = list[0]
    for symbol in list[1:]:
        if symbol == secondborder + 1:
            secondborder = symbol
        else:
            if firstborder == secondborder:
                newlist.append(f"{secondborder}")
                secondborder = firstborder = symbol 
            else:
                newlist.append(f"{firstborder}-{secondborder}")
                secondborder = firstborder = symbol    
    if firstborder + 1 == secondborder:
        newlist.append(f"{firstborder}-{secondborder}")
    if firstborder == secondborder:
        newlist.append(f"{secondborder}") 
    result = ','.join(newlist)
    return f'"{result}"'
list = [2,3,8,9,11,12,13,15,17,19,20,21,25,33,38,44,45,46,50,51,55,77,80,81,90]
print(get_ranges(list))





