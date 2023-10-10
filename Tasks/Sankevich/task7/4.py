import time
def decorator(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения функции {end_time - start_time} секунд')
        return value
    return inner
