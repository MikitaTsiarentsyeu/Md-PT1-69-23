import user_interface as ui
from time_formatting import cur_time
from validation import validate_time_format
from itertools import product
import time


def main():
    MAX_ATTEMPTS = 3
    attempt_count = 0

    res = [f"{h:02d}:{m:02d}" for h, m in product(range(24), range(0, 60, 1))]

    for i in res[:770]:  # Необходимо изменить срез для проверки второй половины
        while attempt_count < MAX_ATTEMPTS:

            time_input = i

            if validate_time_format(time_input):
                formatted_time = cur_time(time_input)

            ui.print_formatted_time(formatted_time)
            time.sleep(0.7)

            break

    ui.print_footer()


if __name__ == "__main__":
    main()
