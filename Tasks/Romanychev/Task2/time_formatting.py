from datetime import datetime
from dictionaries import dict


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
        h1, h2, m1, m2 = [int(h) for i in time_input.split(':') for h in i]
        current_time_str = time_input
    else:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        current_time_str = now.strftime('%H:%M')
        h1, h2, m1, m2 = [int(h)
                          for i in current_time_str.split(':') for h in i]

    match (minute):
        case 0:
            return f"{current_time_str} - {dict[hour % 12][5]} {dict[hour % 12][6]} ровно"
        case m if m <= 20:
            return f"{current_time_str} - {dict[minute][0]} {dict[minute][1]} {dict[(hour + 1) % 12][2]}"
        case m if 21 <= m <= 29:
            return f"{current_time_str} - {dict[20][0]} {dict[m2][0]} {dict[m2][1]} {dict[(hour + 1) % 12][2]}"
        case 30:
            return f"{current_time_str} - половина {dict[(hour + 1) % 12][2]}"
        case m if 31 <= m <= 39:
            return f"{current_time_str} - {dict[30][0]} {dict[m2][0]} {dict[m2][1]} {dict[(hour + 1) % 12][2]}"
        case m if 40 <= m <= 44:
            return f"{current_time_str} - {dict[40][0]} {dict[m2][0]} {dict[m2][1]} {dict[(hour + 1) % 12][2]}"
        case m if m >= 45:
            return f"{current_time_str} - без {dict[60 - minute][3]} {dict[m2][1]} {dict[(hour + 1) % 12][5]}"
        case _:
            return ''
