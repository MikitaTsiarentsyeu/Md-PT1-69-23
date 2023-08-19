def file_to_str():
    try:
        with open('test.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Файл не найден"


print(file_to_str())
