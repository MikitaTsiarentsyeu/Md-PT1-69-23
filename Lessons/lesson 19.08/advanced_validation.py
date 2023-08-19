def validate_number(limit):
    while True:
        number = input(f"Enter your integer value lower then {limit}:\n")
        try:
            number = int(number)
            if number > limit:
                raise RuntimeError("the value you've entered is too high, please try again")
        except ValueError:
            print("you've entered not an integer number, please try again")
        except RuntimeError as e:
            print(e)
        else:
            break
    
    return number

validate_number(100)

