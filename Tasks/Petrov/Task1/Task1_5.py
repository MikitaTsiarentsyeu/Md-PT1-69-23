from random import randint


while True:
    try:        
        left, right = input("Enter borders for a random integer number range: ").split()        
        if int(left) > int(right):
            print("Incorrect borders, try again")
            continue
        else:
            random_number = randint(int(left), int(right))
            print(f"Your number is {random_number}")
            break   
    except:
            print("Wrong input, try again")
            continue
        


