import time

def do_twice(func):
    def new_func():
        func()
        func()
    return new_func

def comment_process(func):
    def wrapper():
        print(f"the {func.__name__} is started")
        func()
        print("the process is finished")
    return wrapper

@do_twice
@comment_process
def test_func():
    print("hello, I'm test func")

# test_func = comment_process(do_twice(test_func))

# test_func()

# test_func = do_twice(test_func)
# test_func()

test_func()

def comment_process(func):
    def wrapper(*args):
        print(f"the {func.__name__} is started")
        res = func(*args)
        print("the process is finished")
        return res
    return wrapper

@comment_process
def sum(x, y):
    return x+y

print(sum(2, 3))

@comment_process
def sum(x, y, z):
    return x+y+z

print(sum(2,3,4))

def time_it(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        global time_res
        time_res = end-start
        return res
    return wrapper

@time_it
def sum(x, y):
    return x+y

x = sum(2, 3)
print(x, time_res)