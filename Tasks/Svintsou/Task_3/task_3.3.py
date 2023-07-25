def count_words(text):
    word_list = text.split()
    return {word: word_list.count(word) for word in word_list}

user_input = input("Введите строку: ")
print("Количество каждого слова в строке:", count_words(user_input))
