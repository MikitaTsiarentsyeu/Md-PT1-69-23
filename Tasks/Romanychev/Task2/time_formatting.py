from dictionaries import dict_min, dict_hour


def cur_time(time_input):
    hour, minute = map(int, time_input.split(':'))
    formatted_time = ""

    # Если время 00:00, то это полночь
    if not (hour or minute):
        formatted_time = f"{time_input} - {dict_hour[hour % 12][2]}"
    elif hour == 12 and not minute:
        formatted_time = f"{time_input} - {dict_hour[hour][2]}"

    # Если минуты равны нулю, то выводим ровное количество часов
    elif minute == 0:
        hour_word = dict_hour[hour % 12][0]
        if hour == 0 or hour % 12 >= 5:
            formatted_time = f"{time_input} - {hour_word} часов ровно"
        elif hour % 12 == 1:
            formatted_time = f"{time_input} - {hour_word} ровно"
        else:
            formatted_time = f"{time_input} - {hour_word} часа ровно"

    # Если минуты меньше 30, то выводим столько-то минут следующего часа
    elif 0 <= hour < 23 and 0 < minute < 30:
        formatted_time = f"{time_input} - {dict_min[minute][0]} минут {dict_hour[hour % 12 + 1][1]}"
    elif hour == 23 and 0 < minute < 30:
        formatted_time = f"{time_input} - {dict_min[minute][0]} минут {dict_hour[hour - 23][1]}"

    # Если минуты равны 30, то выводим половину текущего часа
    elif 0 <= hour < 23 and minute == 30:
        formatted_time = f"{time_input} - половина {dict_hour[hour % 12 + 1][1]}"
    elif hour == 23 and minute == 30:
        formatted_time = f"{time_input} - половина {dict_hour[hour - 23][1]}"

    # Если минуты больше 30 и меньше 45, то выводим столько-то минут следующего часа
    elif 0 <= hour < 23 and 30 < minute < 45:
        formatted_time = f"{time_input} - {dict_min[minute][0]} минуты {dict_hour[hour % 12 + 1][1]}"
    elif hour == 23 and 30 < minute < 45:
        formatted_time = f"{time_input} - {dict_min[minute][0]} минуты {dict_hour[hour - 23][1]}"

    # Если минуты больше или равны 45, то выводим время без такого-то количества минут текущего часа
    elif 0 <= hour < 23 and 45 <= minute <= 58:
        formatted_time = f"{time_input} - без {dict_min[60 - minute][1]} минут {dict_hour[hour % 12][0]}"
    elif 0 <= hour < 23 and minute == 59:
        formatted_time = f"{time_input} - без {dict_min[60 - minute][1]} минуты {dict_hour[hour % 12][0]}"
    elif hour == 23 and 45 <= minute <= 58:
        formatted_time = f"{time_input} - без {dict_min[60 - minute][1]} минут {dict_hour[hour - 23][0]}"
    elif hour == 23 and minute == 59:
        formatted_time = f"{time_input} - без {dict_min[60 - minute][1]} минуты {dict_hour[hour - 23][0]}"

    return formatted_time
