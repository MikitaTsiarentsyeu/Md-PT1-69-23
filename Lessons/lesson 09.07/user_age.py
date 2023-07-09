import datetime

min_age = 18

user_age = input("Enter your birth date mm.yyyy:\n")
user_age = user_age.replace(' ', '')

if len(user_age) != 7 and user_age[2] != '.':
    print("your input has incorrect format")
    exit()

m_y = user_age.split('.')
m = m_y[0]
y = m_y[1]

print(m, y)

if not m.isdigit() or not y.isdigit():
    print("your input has incorrect format")
    exit()

m, y = int(m), int(y)

if m < 1 or m > 12:
    print("your input has incorrect format")
    exit()

current_time = datetime.datetime.now()
print(current_time)

c_m, c_y = current_time.month, current_time.year

if (c_y + (c_m/12)) - (y + (m/12)) >= min_age:
    print("you are old enough")
else:
    print("you are too young for this stuff")