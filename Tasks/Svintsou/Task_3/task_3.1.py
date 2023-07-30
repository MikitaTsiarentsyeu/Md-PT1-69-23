def count_vowels(string):
    vowels = 'aeiouyAEIOUY'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Введите строку: ")
print("Количество гласных в строке:", count_vowels(string))