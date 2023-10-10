def symbols_counter(string):
    
    lower_case = 0
    upper_case = 0

    for i in range(len(string)):
        symbol = string[i]
        if symbol in ''' .,!?()-_'"<>[]{}@#$%^&*;:|/\~`''':
            continue
        elif symbol in 'abcdefghijklmnopqrstuvwxyz':
            lower_case += 1
        else:
            upper_case += 1

    print('lower case symbols = ', lower_case)
    print('upper case case symbols = ', upper_case)

some_string = input('Write some string: \n')

symbols_counter(some_string)    