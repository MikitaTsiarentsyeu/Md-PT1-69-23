numbers = []
even_numbers = []

while True:
    number_to_add = input('type int number')
    if number_to_add == 'done':
        break
    elif number_to_add.isdigit() == True:
        numbers.append(int(number_to_add))
    else:
        print('try one more time')
    
def even_numbers_summ(list, even_list, number_to_add):
    
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            continue
    return sum(even_list)

print(even_numbers_summ(numbers, even_numbers))

