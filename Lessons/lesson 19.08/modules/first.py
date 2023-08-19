print("before import")

# import second as scnd
# from second import test, lst as tsl, func, print_test
from second import *
# print(type(second))

print("after import")

second = "2nd"
# test = 5
# lst = (1,2,3,4,5)
print(__name__)
# print(scnd.__name__)

print(test)
func()
print(lst)
lst.append(10)
print(lst)
func()
print(lst)

new_test = test
test = "new test value"
print(test)
print(new_test)
print_test()