l = [[[1,10,100], (2,20,200), [3,30,300]], [[4,40,400], [5,50,500], [6,60,600]]]

# for i in l:
#     for j in i:
#         for k in j:
#             print(k)

def list_items(l):
    for item in l:
        if isinstance(item, int) or isinstance(item, str):
            print(item)
        else:
            list_items(item)

list_items(l)

# 5! = 1*2*3*4*5
# 4! = 1*2*3*4
# 3! = 1*2*3
# 2! = 1*2
# 1! = 1

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1)*n

print(factorial(5))

n = 12345

def digit_sum(n):
    if n == 0:
        return 0
    return digit_sum(n//10)+n%10

print(digit_sum(n))