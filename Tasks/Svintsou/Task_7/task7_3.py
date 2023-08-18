def sum_even_numbers(numbers):
    try:
        total = sum(num for num in numbers if isinstance(num, int) and num % 2 == 0)
        return total
    except TypeError:
        return "Invalid input type"

input_list = [1, 2, 3, 4, 5, 6]
result = sum_even_numbers(input_list)
print(result)
