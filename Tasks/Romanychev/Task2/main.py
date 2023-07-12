import time
import user_interface as ui
from time_formatting import cur_time
from validation import validate_time_format


def main():
    MAX_ATTEMPTS = 3
    attempt_count = 0

    is_instruction_printed = False  # Флаг для отслеживания вывода инструкции

    while attempt_count < MAX_ATTEMPTS:
        ui.clear_screen()
        ui.print_header()

        if not is_instruction_printed:
            ui.print_instruction()
            is_instruction_printed = True

        ui.print_menu()

        user_choice = input("Ваш выбор (1, 2 или 3): ")
        ui.print_separator()

        match user_choice:
            case "1":
                ui.clear_screen()
                ui.print_header()
                formatted_time = cur_time()
                ui.print_formatted_time(formatted_time)
                ui.print_separator()

                repeat = ui.ask_to_continue()

                match repeat:
                    case "да":
                        continue
                    case "нет":
                        ui.clear_screen()
                        ui.print_header()
                        ui.print_footer()
                        return
                    case "fail":
                        ui.clear_screen()
                        ui.print_header()
                        ui.print_max_attempts_message()
                        ui.print_footer()
                        return

            case "2":
                ui.clear_screen()
                ui.print_header()
                attempt_count = 0

                while attempt_count < MAX_ATTEMPTS:
                    ui.clear_screen()
                    ui.print_header()
                    time_input = input(
                        "Пожалуйста, введите время в формате ЧЧ:ММ\n"
                        "(24-часовой формат): ")
                    ui.print_separator()

                    if validate_time_format(time_input):
                        formatted_time = cur_time(time_input)

                        ui.print_formatted_time(formatted_time)
                        ui.print_separator()

                        repeat = ui.ask_to_continue()

                        match repeat:
                            case "да":
                                attempt_count = 0
                            case "нет":
                                break
                            case "fail":
                                ui.print_max_attempts_message()
                                ui.print_footer()
                                return

                    else:
                        ui.display_invalid_time_error()
                        time.sleep(0.9)
                        attempt_count += 1

            case "3":
                ui.clear_screen()
                ui.print_header()
                ui.print_footer()
                return

        if attempt_count == MAX_ATTEMPTS:
            ui.print_max_attempts_message()

    ui.print_footer()


if __name__ == "__main__":
    main()
