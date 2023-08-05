
def summ(x, y):
    result = (x+y)
    return result


# a = summ(15, 33)
# print(a)


def revers(lstr):
    revl = []
    for element in lstr:
        element = element[::-1]
        revl.append(element)
    return revl


# b = revers(["i want to become a python developer", "it will be hard", "i am learning"])
# print(b)


def char(lstr):
    new_list = []
    for element in lstr:
        if len(element) > 5:
            new_list.append(element)
    return new_list


# c = char(["i want to become a python developer", "name",  "it will be hard", "i am learning", "world", "world1"])
# print(c)


def string_reg(string):
    up = 0
    low = 0
    for element in string:
        if element.isupper():
            up += 1
        elif element.islower():
            low += 1
    return low, up


# d, e = string_reg("I Want To Become A Python Developer!!!")
# print(d, e)


def get_ranges(string):
    k = ""
    while len(string) > 1:

        if string[0] + 1 == string[1]:

            if len(k) == 0:
                k = k + str(string[0]) + "-"
            if len(k) != 0 and k[-1] == ",":
                k = k + str(string[0]) + "-"
            string = string[1:]
        else:
            if len(k) != 0 and k[-1] == "-":
                k = k + str(string[0]) + ","
                string = string[1:]
            else:
                k = k + str(string[0]) + ","
                string = string[1:]

    k = k + str(string[-1])

    return k


# f = get_ranges([-11, 2, 3, 6, 7, 8, 9])
# g = get_ranges([1, 2, 3, 6, 7, 8, 9, 11])
# h = get_ranges([1, 3, 6, 7, 8, 9, 10])
# j = get_ranges([-10, -7, -1])
#
# print(f, type(f))
# print(g, type(g))
# print(h, type(h))
# print(j, type(j))






