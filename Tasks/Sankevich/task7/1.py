n = float(input())

m = float(input())

def division(number1, number2):
    if number2 == 0:
        return "Cannot divide by zero"
    else:
        return number1/number2
    
print(division(n,m))