l = [1,2,3,4,5,6,7,8,9,10,11]

def linear_search(coll, target):
    for i in range(len(coll)):
        if coll[i] == target:
            return i
    return -1

def binary_seacrh(coll, target, low=0, high=None):
    if not high:
        high = len(coll)-1
    if high >= low:
        mid = (low + high) // 2
        if coll[mid] == target:
            return mid
        elif coll[mid] > target:
            return binary_seacrh(coll, target, low, mid-1)
        else:
            return binary_seacrh(coll, target, mid+1, high)
    else:
        return -1
    
print(binary_seacrh(l, 0))