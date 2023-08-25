def even(list):
    sum = 0
    try:
        for i in list:
            if i %2 == 0:
                sum += i
    except TypeError:
        print("Invalid input type")
        exit()
    return print(f'You sum is - {sum}')
even(list=[0,1,4,5,7,9,8,10])
even(list=[0,1,4,'a',7,9,8,'b'])
    