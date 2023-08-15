def even_sum(integers):
    try:
        if not isinstance(integers, list) or not all(type(number) is int for number in integers):
            raise TypeError
        return sum(number for number in integers if number % 2 == 0)
    except TypeError:
        return "Invalid input type"


text = "Processing the sum of all even numbers in "
not_a_list = "test"
not_all_ints = [1, 2, 3.3, 4]
proper_list = [1, 2, 3, 4, 5]
examples = [not_a_list, not_all_ints, proper_list]
for example in examples:
    print(f"{text} {example}")
    print(even_sum(example))
