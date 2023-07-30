""""This file will help to enter a list of ints"""


def enter():
    print('Enter a list of string, example: 1,2,3,12,32 or 1, 2, 3, 12, 32')
    print('It will return a list:')
    print([1, 2, 3, 12, 32])
    str_list = input('Enter: ')
    ans = []
    str_list = str_list.strip().rstrip(',').split(',')
    for _ in str_list:
        if _.strip().isdigit():
            ans.append(int(_))
        else:
            print('Be careful, you can enter only int numbers!')
            return enter()
    return ans
