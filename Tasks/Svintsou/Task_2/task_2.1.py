time = input("Введите время в формате чч:мм: ")
hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)

if minutes == 0:
    print(f"{hours} часов ровно")
elif minutes < 30:
    print(f"{minutes} минут {hours} часа")
elif minutes == 30:
    print(f"половина {hours + 1}")
else:
    print(f"без {60 - minutes} минут {hours + 1}")
time_dict = {}

