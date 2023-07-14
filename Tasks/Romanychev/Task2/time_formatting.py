from datetime import datetime
from dictionaries import dict_min, dict_hour


def convert_time_to_spoken_word(time_input=None):
    """
    Generates a textual representation of the current time or the provided\n
    time input.

    Arguments:
    - time_input (str): Optional. Time in the format "hh:mm". If provided,\n
                        generates the textual representation for the given\n
                        time. If not provided, generates the textual\n

    Returns:
    - str: Textual representation of the time in Russian language.

    """
    if time_input is not None:
        hour, minute = map(int, time_input.split(':'))
        current_time_str = time_input
    else:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        current_time_str = now.strftime('%H:%M')

    match (minute):
        case 0:
            return f"{current_time_str} - {dict_hour[hour % 12][0]} {dict_hour[hour % 12][2]} ровно"
        case m if m < 30:
            return f"{current_time_str} - {dict_min[minute][0]} {dict_min[minute][2]} {dict_hour[(hour + 1) % 12][1]}"
        case 30:
            return f"{current_time_str} - половина {dict_hour[hour % 12 + 1][1]}"
        case m if 30 < m < 45:
            return f"{current_time_str} - {dict_min[minute][0]} {dict_min[minute][2]} {dict_hour[(hour + 1) % 12][1]}"
        case m if m >= 45:
            return f"{current_time_str} - без {dict_min[60 - minute][1]} {dict_min[60 - minute][3]} {dict_hour[(hour + 1) % 12][0]}"
        case _:
            return ""
