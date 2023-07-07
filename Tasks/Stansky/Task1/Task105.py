import random
left = input('Please, input the left border of the range, just an integer:\n')
right = input('Please, input the right border of the range, just an integer:\n')

try:
    left = int(left)
    right = int(right)
    if not left == right:
        if left < right:
            N = random.randint(left, right)
            print(f'Random number in your range is {N}')

        else:
            print('Incorrect input: the right border should be bigger than the left')

    else:
        print(f'If the left border is equal to the right one, than random number in this range is only {left}')
except:
    print('Your input was not an integer number')

