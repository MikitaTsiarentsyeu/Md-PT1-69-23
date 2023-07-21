def remove_vowels(string):
    vowels = "AEIOUYaeiouy"
    return "".join([char for char in string if char not in vowels])

user_input = input("Введите строку: ")
print("Строка c удаленными всеми гласными:", remove_vowels(user_input))