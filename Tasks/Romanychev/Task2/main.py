import os
from dictionaries import dict_min, dict_hour
from validation import validate_time_format, display_invalid_time_error, display_max_attempts_message, ask_to_continue
from time_formatting import cur_time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    MAX_ATTEMPTS = 3  # Максимальное количество попыток ввода времени
    attempt_count = 0  # Счетчик попыток

    while attempt_count < MAX_ATTEMPTS:
        clear_screen()
        print('===========================================================')
        time_input = input('Введите значение времени в формате чч:мм: ')
        print('===========================================================')

        if validate_time_format(time_input):
            # Форматирование времени
            formatted_time = cur_time(time_input, dict_min, dict_hour)
            print('-----------------------------------------------------------')
            print(f'{formatted_time}')
            print('-----------------------------------------------------------')

            repeat = ask_to_continue()  # Запрос на продолжение работы программы
            if repeat == 'нет':
                break
            else:
                attempt_count = 0  # Сброс счетчика попыток
        else:
            # Отображение сообщения об ошибке неверного формата времени
            display_invalid_time_error()
            attempt_count += 1  # Увеличение счетчика попыток

    if attempt_count == MAX_ATTEMPTS:
        # Отображение сообщения о превышении максимального количества попыток
        display_max_attempts_message()


if __name__ == '__main__':
    main()
