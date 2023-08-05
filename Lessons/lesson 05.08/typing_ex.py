def times(a, b):
    return a*b

# int times(float a, float b){ function def in a C-like lang
#     return a*b;
# }

def times_for_int(a:int, b:int) -> int:
    """the function to multiply only int values
    a: int - the first number to multiply
    b: int - the second number to multiply"""
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(times(2, 3))
print(times(2.3, 3.3))
print(times("2", 3))
print(times(["2"], 3))
# print(times(3.3, "2")) error

print(times_for_int(2,3))
print(times_for_int(2,"3"))

print(["1","2","3"] == "123")
print(set(["1","2","3"]) == set("123333333333333"))

def eq(coll1, coll2):
    for item in coll1:
        if item not in coll2:
            return False
    for item in coll2:
        if item not in coll1:
            return False
    return True

def exactly_eq(coll1, coll2):
    if type(coll1) != type(coll2):
        return False
    if len(coll1) != len(coll2):
        return False
    for i in range(len(coll2)):
        if coll1[i] != coll2[i]:
            return False
    return True
    

# int add(int a, int b){
#     return a+b;
# }

# int add(int a, int b, int c){
#     return add(add(a, b), c);
# }

add = 5

add = "test"

def add(a, b):
    return a+b

def add(a, b, c):
    return add(add(a, b), c)

add(1, 2, 3)