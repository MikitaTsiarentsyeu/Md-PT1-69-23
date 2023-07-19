def get_valid_numbers_input():
    while True:
        user_input = input("Enter numbers separated by spaces: ")
        numbers_list = []

        try:
            numbers_list = [float(num) for num in user_input.split()]
            if len(numbers_list) < 2:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter at least two numbers.")
            continue

        return numbers_list


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def main():
    while True:
        numbers_list = get_valid_numbers_input()

        result = calculate_mean(numbers_list)

        print("Mean value:", result)

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
