def divide(a,b):
    try:
        return print(f"You result is - {a/b}") 
    except ZeroDivisionError:
        print("Cannot divide by zero")
divide(a = float(input("Please input the numerator:\n")),b = float(input("Please input the denominator:\n")))
