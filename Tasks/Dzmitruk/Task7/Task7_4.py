import time

def logs(funk):
    """
    a decorator function that logs the execution time,
    arguments and return value of a function to a file.
    """
    def wrapper(*args):
        with open("logs.txt", "a") as f:
            time_start = time.time()
            result = funk(*args)
            time_stop = time.time()
            exec_time = time_stop - time_start
            f.write("Execution time: {}\nArguments: {}\nResult: {}\
                    \n\n".format(exec_time, args, result))
        return result
    return wrapper

@logs
def sum(x, y):
    return x+y


