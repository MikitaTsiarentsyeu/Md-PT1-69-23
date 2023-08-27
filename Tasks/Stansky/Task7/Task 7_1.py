def zero_division(number1, number2):
    try:
        return number1/number2
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except:
        return "Please, check the entered function parameters"



print(zero_division(5, 2))
print(zero_division(5, 0))
print(zero_division(5, 'andrew'))
