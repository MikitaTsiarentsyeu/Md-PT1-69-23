from dictionaries import dict_min, dict_hour


def cur_time(time_input):
    hour, minute = map(int, time_input.split(':'))

    formatted_time = ""  # Инициализация переменной с пустым значением

    match (minute):
        case 0:
            formatted_time = f"{time_input} - {dict_hour[hour % 12][0]} {dict_hour[hour % 12][2]} ровно"
        case m if m < 30:
            formatted_time = f"{time_input} - {dict_min[minute][0]} {dict_min[minute][2]} {dict_hour[(hour + 1) % 12][1]}"
        case 30:
            formatted_time = f"{time_input} - половина {dict_hour[hour % 12 + 1][1]}"
        case m if 30 < m < 45:
            formatted_time = f"{time_input} - {dict_min[minute][0]} {dict_min[minute][2]} {dict_hour[(hour + 1) % 12][1]}"
        case m if m >= 45:
            formatted_time = f"{time_input} - без {dict_min[60 - minute][1]} минут {dict_hour[(hour + 1) % 12][0]}"
        case _:
            formatted_time = ""  # Обработка случая, если ни одно условие\
            # не совпало

    return formatted_time
