import random

def checkNumber(value):
    try:
        return float(value)
    except ValueError:
        print('Invalid value, try again...')
        exit()

value_1 = input("Finger in the stars program:\nEnter your first quantity: ")
szValue_1 = checkNumber(value_1)
value_2 = input("Good... Enter your second quantity: ")
szValue_2 = checkNumber(value_2)
finger = random.uniform(szValue_1, szValue_2)
print(f"""A number "{finger}" is in the range from {szValue_1} to {szValue_2}""")
