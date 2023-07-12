import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_separator():
    separator = "=" * 50  # Используем символ "=" в качестве разделителя
    print(separator)


def print_header():
    print_separator()
    print("   Программа Конвертация Времени. версия 1.0.1")
    print_separator()


# написать краткую инструкцию
def print_instruction():
    print("Инструкция:\n"
          "- Выберите один из вариантов:\n"
          "  1. Вывести текущее время.\n"
          "  2. Ввести время самостоятельно.\n"
          "  3. Завершить программу.\n"
          "- Следуйте инструкциям программы.\n"
          "- После каждого преобразования вы можете выбрать\n "
          "продолжить или выйти."
          )


def print_menu():
    print_separator()
    print("Вывести значение текущего времени - 1")
    print("Ввести время самостоятельно - 2")
    print("Завершить программу - 3")
    print_separator()


def print_max_attempts_message():
    """
    Отображает сообщение о превышении максимального количества попыток.
    """
    clear_screen()
    print_header()
    print(" Превышено количество попыток. Выход из программы.")
    print_separator()


def print_footer():
    print(" Благодарим вас за использование нашей программы!")
    print_separator()


def print_formatted_time(formatted_time):
    print(f"{formatted_time}")


def display_invalid_time_error():
    """
    Отображает сообщение об ошибке неверного формата времени или
    недопустимых значений.
    """
    print('Неверный формат времени или недопустимые значения.\n'
          'Попробуйте снова.')
    print_separator()


def ask_to_continue():
    """
    Запрашивает у пользователя ответ на вопрос о продолжении работы программы.

    Возвращает:
    - str: Ответ пользователя ("да" или "нет").
    """
    max_attempts = 3  # Максимальное количество попыток
    attempt_count = 0  # Счетчик попыток

    while attempt_count < max_attempts:
        response = input('Хотите продолжить? (да/нет): ').lower()

        match response:
            case "да":
                return "да"
            case "нет":
                return 'нет'
            case _:
                attempt_count += 1
                print('Пожалуйста, введите "да" или "нет".')
                if attempt_count == max_attempts:
                    return 'fail'

    return "нет"
