import os


def clear_screen():
    """
    Clears the terminal screen.

    Uses the 'cls' command on Windows operating system (os.name == 'nt'),
    or the 'clear' command on other operating systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_separator():
    """
    Prints a separator line using the "=" symbol as the separator.
    """
    separator_length = 55
    separator = "=" * separator_length
    print(separator)


def print_header():
    """
    Prints the header for the Time Conversion Program.
    """
    print_separator()
    print("       Time Conversion Program. Version 1.0.1")
    print_separator()


def print_instruction():
    """
    Prints the instructions for using the program.
    """
    print("Instructions:\n"
          "- Choose one of the options:\n"
          "  1. Display the current time.\n"
          "  2. Enter the time manually.\n"
          "  3. Exit the program.\n"
          "- Follow the instructions provided by the program.\n"
          "- After each transformation, you can choose to\n "
          "continue or exit."
          )


def print_menu():
    """
    Displays the menu options for the program.
    """
    print_separator()
    print("Display current time - 1")
    print("Enter time manually - 2")
    print("Exit the program - 3")
    print_separator()


def print_max_attempts_message():
    """
    Displays a message indicating that the maximum number of\n
    attempts has been exceeded.
    """
    clear_screen()
    print_header()
    print(" Maximum number of attempts exceeded. Exiting the program.")
    print_separator()


def print_footer():
    """
    Prints the footer message to thank the user for using the program.
    """
    print(" Thank you for using our program!")
    print_separator()


def display_invalid_time_error():
    """
    Displays an error message for an invalid time format or
    invalid values.
    """
    print('Invalid time format or invalid values.\n'
          'Please try again.')
    print_separator()


def ask_to_continue():
    """
    Checks if the user wants to continue program execution.

    Returns:
        str: Returns "yes" if the user wants to continue,
             "no" if the user does not want to continue,
             or "fail" if the maximum number of attempts is reached.

    """
    MAX_ATTEMPTS = 3  # Maximum number of attempts
    attempt_count = 0  # Attempt counter

    while attempt_count < MAX_ATTEMPTS:
        response = input('Would you like to continue? (yes/no): ').lower()

        match response:
            case "yes":
                return "yes"
            case "no":
                return 'no'
            case _:
                attempt_count += 1
                print('Please enter "yes" or "no".')
                if attempt_count == MAX_ATTEMPTS:
                    return 'fail'

    return "no"
