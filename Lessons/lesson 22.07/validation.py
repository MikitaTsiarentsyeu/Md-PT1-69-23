while True:
    user_input = input("Input the data in the format hh:mm\n")

    if len(user_input) != 5:
        print("incorrect input, the value is of wrong length")
        continue

    if user_input[2] != ':':
        print("incorrect input, the value lacks the : sign")
        continue

    values = user_input.split(':')

    if len(values) != 2:
        print("incorrect input, the : sign should present only once")
        continue

    hours, minutes = values[0], values[1]

    if not (hours.isdigit() and minutes.isdigit()):
        print("the hours and the minutes values must be digits")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 23 or minutes > 59:
        print("incorrect hours or minutes values")
        continue

    break

print("main logic goes here")