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
    list_of_num = list(set(list_of_num))
    list_of_num.sort()
                       
    start = stop = list_of_num[0]

    for i in range(1, len(list_of_num)):
        if list_of_num[i] == stop + 1:
            stop = list_of_num[i]
        else:
            if start == stop:
                ranges += str(start) + ", "
            else:
                ranges += str(start) + "-" + str(stop) + ", " 
            start = stop = list_of_num[i]
            
    if start == stop:
        ranges += str(start) 
    else:
        ranges += str(start) + "-" + str(stop) 

    return ranges
