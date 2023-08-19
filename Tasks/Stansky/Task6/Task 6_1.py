str_rev = input('Please, input string to reverse:\n')


def string_rev(str_rev):
    if len(str_rev) == 1:
        return str_rev
    return str_rev[-1] + string_rev(str_rev[0:-1])


print(string_rev(str_rev))

