import time
import user_interface as ui
from time_formatting import cur_time
from validation import validate_time_format


def main():
    MAX_ATTEMPTS = 3
    attempt_count = 0

    while attempt_count < MAX_ATTEMPTS:
        ui.clear_screen()
        ui.print_header()

        time_input = input("Пожалуйста, введите время в формате ЧЧ:ММ \n"
                           "(24-часовой формат):  ")
        ui.print_separator()

        if validate_time_format(time_input):
            formatted_time = cur_time(time_input)

            ui.print_formatted_time(formatted_time)
            ui.print_separator()

            repeat = ui.ask_to_continue()
            if repeat == "нет":
                break

        else:
            ui.display_invalid_time_error()
            time.sleep(0.8)
            attempt_count += 1

        if attempt_count == MAX_ATTEMPTS:
            ui.print_max_attempts_message()

    ui.print_footer()


if __name__ == "__main__":
    main()
