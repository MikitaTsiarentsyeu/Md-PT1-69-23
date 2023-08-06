def level1():
    print("before level 1")
    level2()
    print("after level 1")

def level2():
    print("\tbefore level 2")
    level3()
    print("\tafter level 2")

def level3():
    print("\t\tbefore level 3")
    level4()
    print("\t\tafter level 3")

def level4():
    print("\t\t\tbefore level 4")
    # level1()
    print("\t\t\tafter level 4")

# level1()

def level(n=1, max=3):
    if n > max:
        return
    print('\t'*(n-1)+f"before level {n}")
    level(n+1, max)
    # print('\t'*(n-1)+f"after level {n}")

level()