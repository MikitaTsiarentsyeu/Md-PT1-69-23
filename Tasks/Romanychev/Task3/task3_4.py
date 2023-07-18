import ast


def get_nth_largest(numbers, n):
    """
    Get the nth largest number from the list of numbers.

    Args:
        numbers (list): The list of numbers.
        n (int): The position of the desired largest number (1-indexed).

    Returns:
        float: The nth largest number, or None if the list doesn't have enough elements.

    """
    # Check if all elements in the list are numeric (int or float)
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("The list should contain only numeric values.")

    if len(numbers) < n:
        return None

    unique_numbers = sorted(set(numbers), reverse=True)
    if n > len(unique_numbers):
        return None

    return unique_numbers[n - 1]


def user_input_to_list(user_input):
    try:
        numbers_list = ast.literal_eval(user_input)
        if not isinstance(numbers_list, list):
            numbers_list = [numbers_list]
    except (ValueError, SyntaxError):
        numbers_list = [float(num) for num in user_input.split()]
    return numbers_list


def get_valid_numbers_input():
    while True:
        user_input = input(
            "Enter numbers in the format [1, 2, 3] or separated by spaces: ")
        try:
            numbers_list = user_input_to_list(user_input)
            if len(numbers_list) < 2:
                print(
                    "The list should contain more than one number. Please enter the list again.")
            else:
                return numbers_list
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter numbers in the correct format.")


def main():
    while True:
        try:
            numbers_list = get_valid_numbers_input()

            while True:
                try:
                    max_number_index = int(
                        input(f"Enter the position of the largest number from the end (1-{len(numbers_list)}): "))
                    if max_number_index < 1 or max_number_index > len(numbers_list):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid position. Please enter a number from 1 to", len(
                        numbers_list))

            result = get_nth_largest(set(numbers_list), max_number_index)

            if result is not None:
                print(
                    f"The {max_number_index}-th largest number from the end in the list:", result)
            else:
                print("The list does not have enough elements.")

        except ValueError as e:
            print(f"Error: {e}")

        while True:
            choice = input("Do you want to continue? (yes/no): ").lower()
            if choice == "yes" or choice == "no":
                break
            else:
                print("Please enter only 'yes' or 'no'.")

        if choice == "no":
            break


if __name__ == "__main__":
    main()
