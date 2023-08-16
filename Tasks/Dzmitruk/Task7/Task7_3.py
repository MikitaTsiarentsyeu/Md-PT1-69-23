
def sum_all_numbers(num_list):
    """
    a function that takes a list of integers as input \
    and returns the sum of all even numbers in the list
    """
    try:
        sum_num = 0
        for num in num_list:
            sum_num += num
        return print(sum_num)
    except TypeError:
        return print("Invalid input type.")

                 
sum_all_numbers([1,2,3])