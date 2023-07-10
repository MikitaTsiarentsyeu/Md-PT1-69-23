import re


def validate_time_format(time_input):
    """
    Проверяет корректность формата ввода времени.

    Аргументы:
    - time_input (str): Время в формате "чч:мм".

    Возвращает:
    - bool: True, если формат ввода времени корректный, иначе False.
    """
    pattern = r'^\d{2}:\d{2}$'
    if re.match(pattern, time_input):
        hour, minute = map(int, time_input.split(':'))
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            return True
    return False


def validate_yes_no_input(input_str):
    """
    Проверяет корректность ответа на вопрос с ответом "да" или "нет".

    Аргументы:
    - input_str (str): Строка с вопросом.

    Возвращает:
    - str: Ответ пользователя ("да" или "нет").
    """
    while True:
        response = input(input_str).lower()
        if response == 'да' or response == 'нет':
            return response
        else:
            print('Пожалуйста, введите "да" или "нет".')


def display_invalid_time_error():
    """
    Отображает сообщение об ошибке неверного формата времени или недопустимых значений.
    """
    print('Неверный формат времени или недопустимые значения. Попробуйте снова.')


def display_max_attempts_message():
    """
    Отображает сообщение о превышении максимального количества попыток.
    """
    print('Превышено количество попыток. Выход из программы.')


def ask_to_continue():
    """
    Запрашивает у пользователя ответ на вопрос о продолжении работы программы.

    Возвращает:
    - str: Ответ пользователя ("да" или "нет").
    """
    while True:
        response = input('Хотите продолжить? (да/нет): ').lower()
        if response == 'да' or response == 'нет':
            return response
        else:
            print('Пожалуйста, введите "да" или "нет".')
