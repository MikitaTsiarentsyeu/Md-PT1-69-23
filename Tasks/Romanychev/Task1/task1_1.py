import time
import temp_converter
import utilities as util


def validate_temperature_input(temperature):
    try:
        float(temperature)
        return True
    except ValueError:
        return False


def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()


def main():
    util.print_slow("==============================================")
    util.print_slow("Welcome to the Temperature Conversion Program!")
    util.print_slow("==============================================")
    util.print_slow("Instructions:")
    util.print_slow(
        "- Choose the temperature type: C - Celsius, F - Fahrenheit.")
    util.print_slow("- Enter the temperature value when prompted.")
    util.print_slow("- The program will convert the temperature and "
                    "display the result.")
    util.print_slow(
        "- You can choose to continue or exit after each conversion.")
    util.print_slow(
        "============================================================")

    while True:
        option = input("Please select the temperature type "
                       "(C - Celsius, F - Fahrenheit): ")

        if option.upper() == "C":
            while True:
                celsius = input("Enter the temperature in Celsius: ")
                if util.validate_temperature_input(celsius):
                    break
                else:
                    print("Invalid temperature value. "
                          "Please enter a valid number.")

            celsius = float(celsius)
            fahrenheit = temp_converter.celsius_to_fahrenheit(celsius)
            print("The temperature in Fahrenheit is:", round(fahrenheit, 2))
            print()

        elif option.upper() == "F":
            while True:
                fahrenheit = input("Enter the temperature in Fahrenheit: ")
                if util.validate_temperature_input(fahrenheit):
                    break
                else:
                    print("Invalid temperature value. "
                          "Please enter a valid number.")

            fahrenheit = float(fahrenheit)
            celsius = temp_converter.fahrenheit_to_celsius(fahrenheit)
            print("The temperature in Celsius is:", round(celsius, 2))
            print()

        else:
            print("Invalid temperature type. Please choose C for Celsius "
                  "or F for Fahrenheit.")
            continue

        while True:
            choice = input("Do you want to continue with another conversion?"
                           " (Yes/No): ").lower()
            if choice == "yes" or choice == "no":
                break
            else:
                print("Invalid choice. Please enter Yes or No.")

        if choice == "no":
            util.print_slow("Thank you for using the Temperature Conversion "
                            "Program. Goodbye!")
            break


if __name__ == "__main__":
    main()
