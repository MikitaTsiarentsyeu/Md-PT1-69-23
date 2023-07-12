from datetime import datetime
from dictionaries import dict_min, dict_hour


def cur_time(time_input=None):
    if time_input is not None:
        hour, minute = map(int, time_input.split(':'))
    else:
        now = datetime.now()
        hour = now.hour
        minute = now.minute

    formatted_time = ""  # Инициализация переменной с пустым значением

    match (minute):
        case 0:
            formatted_time = f"{time_input or now.strftime('%H:%M')} - {dict_hour[hour % 12][0]} {dict_hour[hour % 12][2]} ровно"
        case m if m < 30:
            formatted_time = f"{time_input or now.strftime('%H:%M')} - {dict_min[minute][0]} {dict_min[minute][2]} {dict_hour[(hour + 1) % 12][1]}"
        case 30:
            formatted_time = f"{time_input or now.strftime('%H:%M')} - половина {dict_hour[hour % 12 + 1][1]}"
        case m if 30 < m < 45:
            formatted_time = f"{time_input or now.strftime('%H:%M')} - {dict_min[minute][0]} {dict_min[minute][2]} {dict_hour[(hour + 1) % 12][1]}"
        case m if m >= 45:
            formatted_time = f"{time_input or now.strftime('%H:%M')} - без {dict_min[60 - minute][1]} {dict_min[60 - minute][3]} {dict_hour[(hour + 1) % 12][0]}"
        case _:
            formatted_time = ""

    return formatted_time
