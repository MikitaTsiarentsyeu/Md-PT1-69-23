x = "global value"

def outer():
    print("this is outer func")
    x = "outer value"
    print(x)
    def inner():
        nonlocal x
        x = "inner value"
        print(x)
        print("this is inner func")
    inner()
    print(x)

outer()
print(x)