import datetime

def logs(func):
    """
    :param func: *args, start_time, end_time, file: 'Task7_4-logs.txt', result func summ_value
    :return: function that logs the execution time, arguments and return value of a function to a file.
    """
    def wrapper(*args):
        with open('Task7_4-logs.txt', 'a') as f:
            start_time = datetime.datetime.now()
            result = func(*args)
            end_time = datetime.datetime.now()
            amount_time = end_time - start_time
            f.write('Amount of time: {}\n'.format(amount_time))
            f.write('Arguments: {}\n'.format(args))
            f.write('Result: {}\n'.format(result))
            f.write('\n')
        return result
    return wrapper

@logs
def summ_value(a: float, b: float) -> float:
    """
    :return: sum of values a and b
    """
    return a + b

summ_value(19, 1)

