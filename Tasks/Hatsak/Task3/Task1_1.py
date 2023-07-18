"""1. Write a program that takes a string as input from a user and returns the number of vowels in the string."""
import Task1_1_tests
import time

vowels = ['a', 'e', 'o', 'u', 'y', 'i', 'A', 'E', 'O', 'U', 'Y', 'I']
my_str = Task1_1_tests.cases[0]
# my_str = input("Enter any string")
my_str = my_str.strip()


def KortezR(function):
    def wrapped(*args):
        print("Это решение было предложено @KortezR в телеграме!")
        res = function(*args)
        print("Спасибо за такой вариант!")
        return res
    return wrapped


def branch(number_of_repeats=10000):
    def time_of_function(function):
        def wrapped(*args):
            start_time = time.time()
            for i in range(number_of_repeats):
                res = function(*args)
            end_time = time.time()
            print(round(end_time - start_time, 3))
            return res
        return wrapped
    return time_of_function


@branch()
def try1(s):
    return s.replace('a', '').replace('o', '').replace('e', '').replace('i', '').replace('u', '').replace('y', '').replace('A', '').replace('O', '').replace('E', '').replace('I', '').replace('U', '').replace('Y', '')


@branch()
def try2(s):
    ans = []
    for l in s:
        if l in vowels:
            continue
        ans.append(l)
    return ''.join(ans)


@branch()
def try3(s):
    for vowel in vowels:
        s = ''.join(s.split(vowel))
    return s


@branch()
def try4(s):
    return ''.join([l for l in s if l not in vowels])


def try5(s):
    for v in vowels:
        if v in s:
            return try5(s[0:s.index(v)]) + try5(s[s.index(v)+1:])
    return s


@KortezR
def try6(s):
    if len(s) == 1:
        return 1 if s in vowels else 0
    else:
        return try6(s[-1]) + try6(s[:-1])


#print(branch()(try5)(my_str))
print(try6(my_str))
# 0.325
# 3.792
# 0.507
# 2.695
# 6.238
