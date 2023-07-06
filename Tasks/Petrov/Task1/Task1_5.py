from random import randint


while True:
    try:
        print("Enter borders for a random integer number range", end=": ")
        left, right = input().split()
        if int(left) > int(right):
            print("Incorrect borders, try again")
            continue
        else:
            random_number = randint(int(left), int(right))
            print(f"Your number is {random_number}")
            break
    except ValueError:
        print("Wrong input, try again")
        continue
