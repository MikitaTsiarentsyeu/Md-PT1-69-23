def sum(a, b):
    
    return (a+b)

def revers (list):
    new_list = []

    for string in list:
        new_list.append(string[::-1])
    
    return new_list

def greater5 (list):
    new_list = []

    for string in list:
        if len(string) > 5:
            new_list.append(string)
       
    return new_list

def countlowup (string):
    low = 0
    up = 0

    for char in string:
        if char.isalpha():
            if char == char.upper():
                up += 1
            else:
                low += 1
        else:
            continue
                                         
    return (print("Lower case symbols -", low,", upper case symbols -", up))

def get_ranges(list_of_num):
    ranges = ""
    start = stop = ""
    list_of_num = list(set(list_of_num)) 
    list_of_num.sort() 

    for i in range(len(list_of_num)-1):

        if list_of_num[i+1] != list_of_num[i] + 1:
            stop = str(list_of_num[i])
            ranges += stop + ","

        else:
            start = str(list_of_num[i])
            ranges += start + "-"

    ranges += str(list_of_num[i+1])

    ranges = ranges.split(",")

    new_ranges = []

    for new_range in ranges:
        if new_range.count("-") > 1:
            number = new_range.split("-")
            new_ranges.append(number[0] + "-" + number[-1])
        else:
            new_ranges.append(new_range)

    new_ranges = ', '.join(new_ranges)
    
    return new_ranges