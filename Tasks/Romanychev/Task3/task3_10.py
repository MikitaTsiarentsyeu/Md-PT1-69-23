import random
import time

# Function to perform the Miller-Rabin primality test


def miller_rabin_primality_test(n, k=5):
    if n < 2:
        return False
    if n < 4:
        return True

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not check(a, s, d, n):
            return False
    return True

# User Interface


def get_user_choice():
    while True:
        print("1. Enter numbers manually")
        print("2. Generate an ordered or random list")
        print("3. Create a generator")
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Process user's choice


def process_choice(choice):
    if choice == "1":
        numbers_list = get_manual_numbers_list()
    elif choice == "2":
        while True:
            print("Select the type of random list to generate:")
            print("1. Ordered list from 1 to the upper limit")
            print("2. Random list with specified length")
            sub_choice = input("Enter your choice (1 or 2): ").strip()

            if sub_choice == "1":
                upper_limit = get_generator_upper_limit()
                numbers_list = generate_ordered_list(upper_limit)
                break
            elif sub_choice == "2":
                list_length = get_random_list_length()
                upper_limit = list_length
                numbers_list = generate_random_list(upper_limit, list_length)
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
    elif choice == "3":
        upper_limit = get_generator_upper_limit()
        numbers_list = generate_numbers(upper_limit)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return None

    return numbers_list

# Ask if the user wants to continue


def continue_program():
    while True:
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice in ["yes", "no"]:
            return choice
        else:
            print("Please enter 'yes' or 'no'.")

# Function to generate a list of numbers in descending order


def generate_numbers(upper_limit):
    num = upper_limit
    while num >= 1:
        yield num
        num -= 1

# Function to generate an ordered list from 1 to the specified upper limit


def generate_ordered_list(upper_limit):
    return list(range(1, upper_limit + 1))

# Function to generate a random list of specified length with numbers from 1 to the upper limit


def generate_random_list(upper_limit, list_length):
    random_list = [random.randint(1, upper_limit) for _ in range(list_length)]
    return list(set(random_list))

# Function to manually input numbers from the user


def get_manual_numbers_list():
    while True:
        user_input = input(
            "Enter numbers separated by spaces or a list (e.g. [1, 2, 3]): ")
        numbers_list = []
        try:
            if "[" in user_input and "]" in user_input:
                numbers_list = [int(num)
                                for num in user_input[1:-1].split(",")]
            else:
                numbers_list = [int(num) for num in user_input.split()]
        except ValueError:
            print("Invalid input. Please enter only numbers or a valid list.")
            continue
        return sorted(numbers_list)

# Decorator to measure execution time of functions


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time: {:.6f} seconds".format(execution_time))
        return result
    return wrapper

# Validation functions


def get_random_list_length():
    while True:
        list_length_input = input("Enter the length of the random list: ")
        try:
            list_length = int(list_length_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if list_length <= 0:
            print("Invalid input. Please enter a positive integer.")
            continue

        return list_length


def get_generator_upper_limit():
    while True:
        upper_limit_input = input(
            "Enter the upper limit for generating numbers: ")
        try:
            # Use eval to evaluate scientific notation and obtain the actual value
            upper_limit = eval(upper_limit_input)
            if not isinstance(upper_limit, int) or upper_limit <= 0:
                raise ValueError()
        except (ValueError, SyntaxError):
            print(
                "Invalid input. Please enter a positive integer or valid scientific notation (e.g., 1*10**20).")
            continue

        return upper_limit

# Function to find the largest prime number in the list


@measure_execution_time
def get_largest_prime(numbers_list):
    largest_prime = None

    if isinstance(numbers_list, list):
        for num in reversed(numbers_list):
            if miller_rabin_primality_test(num):
                largest_prime = num
                break
    elif isinstance(numbers_list, range):
        for num in numbers_list:
            if miller_rabin_primality_test(num):
                largest_prime = num
                break
    else:
        for num in numbers_list:
            if miller_rabin_primality_test(num):
                largest_prime = num
                break

    return largest_prime

# Main function to run the program


def main():
    while True:
        choice = get_user_choice()
        numbers_list = process_choice(choice)

        if numbers_list is None:
            continue

        print("Your list:", numbers_list)

        largest_prime = get_largest_prime(numbers_list)
        if largest_prime is not None:
            print("The largest prime number in the list:", largest_prime)
        else:
            print("No prime numbers found in the list.")

        choice = continue_program()
        if choice == "no":
            break


if __name__ == "__main__":
    main()
