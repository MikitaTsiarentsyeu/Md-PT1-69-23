from time import time, sleep

def timemometr(func):
    def wrapper(*args):
        start_time = time()
        value = func(*args)
        end_time = time()
        print(f'Время выполнения функции {end_time - start_time} секунд')
        return value
    return wrapper

@timemometr
def summa(a, b):
    return a + b

print(summa(3, 3))
