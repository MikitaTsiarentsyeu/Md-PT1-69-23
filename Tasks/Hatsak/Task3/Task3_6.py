"""6. Write a program that takes a string as input and returns the string with all vowels removed."""
import Task3_6_tests
import time

vowels = ['a', 'e', 'o', 'u', 'y', 'i', 'A', 'E', 'O', 'U', 'Y', 'I']
my_str = Task3_6_tests.cases[0]

my_str = my_str.strip()


def branch(number_of_repeats=10000):
    def time_of_function(function):
        def wrapped(*args):
            start_time = time.time()
            for i in range(number_of_repeats):
                res = function(*args)
            end_time = time.time()
            dt = (round(end_time - start_time, 3))
            return dt
        return wrapped
    return time_of_function


def try1(s):
    return s.replace('a', '').replace('o', '').replace('e', '').replace('i', '').replace('u', '').replace('y', '').replace('A', '').replace('O', '').replace('E', '').replace('I', '').replace('U', '').replace('Y', '')


def try2(s):
    ans = []
    for l in s:
        if l in vowels:
            continue
        ans.append(l)
    return ''.join(ans)


def try3(s):
    for vowel in vowels:
        s = ''.join(s.split(vowel))
    return s


def try4(s):
    return ''.join([l for l in s if l not in vowels])


print('\nHello, this program will delete all vowels from Walt Whitman poem "O Captain! My Captain!"\n\n\n')
print(my_str)
print('\n\n\nBut you can choose you own text. Type "u" to eneter user\'s text!')
enter = input('Or anything else to continue with default text: ')
if enter.lower() in ('u', 'г'):
    my_str = input('Fine! Enter your text: ')
ans = try1(my_str)
print(ans)
print('\n\n\nDo you want to know which functions works faster? I think you do!')
print('try1 will delete all vowels 10000 times for: ')
print(branch()(try1)(my_str))
print('try2 will delete all vowels 10000 times for: ')
print(branch()(try2)(my_str))
print('try3 will delete all vowels 10000 times for: ')
print(branch()(try3)(my_str))
print('try4 will delete all vowels 10000 times for: ')
print(branch()(try4)(my_str))


# my_str = input("Enter any string")