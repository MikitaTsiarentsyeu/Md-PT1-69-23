def reverse_strings_in_list(input_list):
    reversed_list = [string[::-1] for string in input_list]
    return reversed_list

string_list = ["hello", "world", "python"]
reversed_strings = reverse_strings_in_list(string_list)
print("Перевернутые строки:", reversed_strings) 
