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


def swap_case(input_str):
    return input_str.swapcase()


def main():
    while True:
        user_input = get_valid_input()
        swapped_str = swap_case(user_input)
        print("Swapped string:", swapped_str)

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
