def is_valid_input(input_str):
    words = input_str.split()
    return all(word.isalpha() for word in words)


def get_valid_input():
    while True:
        user_input = input("Enter a string: ")
        if is_valid_input(user_input):
            return user_input
        else:
            print("Invalid input. Please enter only words.")


def reverse_string(input_str):
    return input_str[::-1]


def main():
    while True:
        user_input = get_valid_input()
        reversed_str = reverse_string(user_input)
        print("Reversed string:", reversed_str)

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
