import re


def remove_vowels(input_string, vowels):
    return ''.join(char for char in input_string if char.lower() not in vowels)


def get_valid_input():
    while True:
        user_input = input("Enter a string: ")

        # Use regex to check if the input contains any characters (including symbols and spaces)
        if re.match(r'^[^\n]+$', user_input):
            return user_input
        else:
            print("Invalid input. Please enter a valid string.")


def choose_language():
    while True:
        language = input(
            "Choose the language of the input string:\n'en' - English,\n'ru' - Russian,\n"
            "'pl' - Polish,\n'de' - German,\n'fr' - French.\nYour choice: ")
        if language in ['en', 'ru', 'pl', 'de', 'fr']:
            return language
        else:
            print("Invalid choice. Please select from the provided languages.")


def main():
    while True:
        language = choose_language()
        vowels = {
            'en': ['a', 'e', 'i', 'o', 'u'],
            'ru': ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'],
            'pl': ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y'],
            'de': ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü'],
            'fr': ['a', 'e', 'i', 'o', 'u']
        }

        user_input = get_valid_input()

        result = remove_vowels(user_input, vowels[language])

        print("String without vowels:", result)

        while True:
            choice = input("Do you want to continue? (yes/no): ").lower()
            if choice in ["yes", "no"]:
                break
            else:
                print("Please enter 'yes' or 'no'.")

        if choice == "no":
            break


if __name__ == "__main__":
    main()
