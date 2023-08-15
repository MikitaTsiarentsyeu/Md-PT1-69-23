import time


def logs(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        execution_time = time.perf_counter() - start_time
        with open("logs7_4.txt", "w", encoding="UTF-8") as file:
            file.write(f"{func.__name__} was called\nArguments of this function: {args}\nExecution time: {execution_time:.8f} sec\nResult: {result}")
        return result
    return wrapper


@logs
def positive_args_sum(*args):
    return sum(filter(lambda x: x > 0, args))


positive_args_sum(-1, 2, -3, 4, 5)
