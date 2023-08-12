def outer():
    def inner():
        print("this is inner func")
    return inner

new_func = outer()
# new_func()

def operation(sign):
    if sign == '+':
        def oper(a, b):
            return a+b
    elif sign == "*":
        def oper(a, b):
            return a*b
    return oper
        
mult = operation('*')
# print(mult(2, 3))




def power_n(n):
    test_var = "test"
    def action(x):
        print(test_var)
        return x**n
    action(2)
    return action

square = power_n(2)
print(type(square))
print(square(2))

for i in range(11):
    print(power_n(i)(2))

def operation(sign):
    def oper(a, b):
        if sign == '+':
            return a+b
        elif sign == "*":
            return a*b
    return oper