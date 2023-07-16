from time import strptime
from dictionary import time_dict as words


# def checktime(possible_time): <----------------------------- works too
#     if len(possible_time) != 5:
#         print("Incorrect input, try again")
#         return False
#     elif possible_time[2] != ":":
#         print("Incorrect input, try again")
#         return False
#     elif not possible_time[0:2].isdigit() or not possible_time[3:].isdigit():
#         print("Incorrect input, try again")
#         return False
#     elif int(possible_time[0:2]) > 23 or int(possible_time[3:]) > 59:
#         print("Incorrect input, try again")
#         return False
#     else:
#         print("Alright")
#         return True


def checktime(possible_time):
    try:
        strptime(possible_time, "%H:%M")
        print("Alright")
        return True
    except ValueError:
        print("Incorrect input, try again")
        return False


while True:
    given_time = input("Input the time in hh:mm format: ")
    if checktime(given_time):
        break

hours, minutes = map(int, given_time.split(":"))

hours_12 = hours if hours < 12 else abs(12 - hours)
if minutes == 0:
    print(f"{given_time} - {words[12][2] if hours_12 == 0 else words[hours_12][2]} ровно")
elif minutes < 30:
    print(f"{given_time} - {words[minutes][0]} {words[hours_12+1][3]}")
elif minutes == 30:
    print(f"{given_time} - половина {words[hours_12+1][3]}")
elif 45 > minutes > 30:
    print(f"{given_time} - {words[minutes][0]} {words[hours_12+1][3]}")
else:
    print(f"{given_time} - без {words[60-minutes][1]} {words[hours_12+1][2].split()[1] if hours_12 == 0 else words[hours_12+1][2].split()[0]}")
