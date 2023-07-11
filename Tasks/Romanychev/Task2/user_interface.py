import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    print("================================================")
    print("   Программа Конвертация Времени. версия 1.0.0")
    print("================================================\n")


def print_max_attempts_message():
    """
    Отображает сообщение о превышении максимального количества попыток.
    """
    print("================================================")
    print("Превышено количество попыток. Выход из программы.")


def print_footer():
    print("================================================")
    print(" Спасибо, что воспользовались нашей программой!")
    print("================================================\n")


def print_separator():
    print("------------------------------------------------")


def print_formatted_time(formatted_time):
    print(f"{formatted_time}")


def display_invalid_time_error():
    """
    Отображает сообщение об ошибке неверного формата времени или
    недопустимых значений.
    """
    print('Неверный формат времени или недопустимые значения.\n'
          'Попробуйте снова.')


def ask_to_continue():
    """
    Запрашивает у пользователя ответ на вопрос о продолжении работы программы.

    Возвращает:
    - str: Ответ пользователя ("да" или "нет").
    """
    max_attempts = 3  # Максимальное количество попыток
    attempt_count = 0  # Счетчик попыток

    while attempt_count <= max_attempts:
        response = input('Хотите продолжить? (да/нет): ').lower()
        if response == "нет":
            return "нет"
        elif response == "да":
            return response
        else:
            print('Пожалуйста, введите "да" или "нет".')
            attempt_count += 1
            if attempt_count == max_attempts:
                print_max_attempts_message()
                return "нет"

    # Достигнуто макс. кол-во попыток или введен ответ отличный от "да"
    return 'нет'
