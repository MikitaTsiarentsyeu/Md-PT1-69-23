flag = True
list_of_something = []
summ = 0

while flag == True:
    add_number_or_done = input('Gimme some number or print "done": ')
    if add_number_or_done == 'done':
        break

    if '.' in add_number_or_done:
        some_list_i_guess = add_number_or_done.split('.')
        for check in range(len(some_list_i_guess)):
            if some_list_i_guess[check].isdigit() == False:
                print('i said gimme number')
                continue
            else:
                add_number_or_done = float(add_number_or_done)
                list_of_something.append(add_number_or_done)
                break

    elif ',' in add_number_or_done:
        some_list_i_guess = add_number_or_done.split(',')
        for check in range(len(some_list_i_guess)):
            if some_list_i_guess[check].isdigit() == False:
                print('i said gimme number')
                continue
            else:
                add_number_or_done = some_list_i_guess[0] + '.' + some_list_i_guess[1]
                add_number_or_done = float(add_number_or_done)
                list_of_something.append(add_number_or_done)
                break

    elif ',' not in add_number_or_done or '.' not in add_number_or_done:
        while add_number_or_done.isdigit() == False:
            print("it's not a number")
            break
        else:
            add_number_or_done = float(add_number_or_done)
            list_of_something.append(add_number_or_done)

print(list_of_something)

list_largest_number = max(list_of_something)

list_of_something.remove(max(list_of_something))

print('The second largest number is', max(list_of_something))

list_of_something.append(list_largest_number)

print(list_of_something)


        
