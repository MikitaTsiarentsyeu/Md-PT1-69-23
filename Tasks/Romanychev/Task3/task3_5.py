def is_valid_input(input_list):
    return all(word.isalpha() for word in input_list)


def get_valid_input():
    while True:
        user_input = input("Enter a list of strings (separated by spaces): ")
        input_list = user_input.split()
        if is_valid_input(input_list):
            return input_list
        else:
            print("Invalid input. Please enter only words.")


def filter_strings(input_list):
    return [string for string in input_list if len(string) > 5]


def main():
    while True:
        user_input = get_valid_input()
        filtered_list = filter_strings(user_input)
        print("Filtered list:", filtered_list)

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
