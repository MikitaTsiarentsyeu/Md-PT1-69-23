import time


def write_param(func):
    def wrapper(*args):
        start_work = time.time()
        result = func(*args)
        end_work = time.time()
        time_work = end_work-start_work
        with open("LogsFunc.txt", "w") as file:
            file.write(f'Logs of function "{func.__name__}":\n'
            f'The function has arguments: {args} \n'
            f'Function execution time {time_work:4f} seconds:\nFunction execution result: {result}')
        return result
    return wrapper


@write_param
def sum_elem(*num_list):
    sum = 0
    for element in num_list:
        sum += element
    sum = sum**3
    return sum


sum_elem(0, 20, 448, 5687, 14687963)



