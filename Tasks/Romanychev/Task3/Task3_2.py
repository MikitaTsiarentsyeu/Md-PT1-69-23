# Function to calculate the sum of all even numbers in the given list
def get_even_sum(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum

# Main function to handle user input and display the result


def main():
    while True:
        try:
            # Ask the user to input numbers separated by spaces
            user_input = input("Enter numbers separated by spaces: ")

            # Convert the input string into a list of integers
            numbers_list = [int(num) for num in user_input.split()]

            # Check if the list contains at least two numbers
            if len(numbers_list) < 2:
                print("Please enter at least two numbers.")
                continue  # Prompt the user to enter numbers again

            # Calculate the sum of all even numbers in the list using the get_even_sum function
            result = get_even_sum(numbers_list)

            if result == 0:
                print("There are no even numbers in the list.")
            else:
                # Display the result
                print("Sum of all even numbers in the list:", result)

        except ValueError:
            # Handle the case where the user input contains non-numeric characters
            print("Input error. Please enter only numbers separated by spaces.")
            continue  # Prompt the user to enter numbers again

        except KeyboardInterrupt:
            # Handle the case where the user interrupts the program (e.g., with Ctrl+C)
            print("\nProgram terminated by user.")
            break

        # Ask the user if they want to continue or exit the program
        while True:
            choice = input("Do you want to continue? (yes/no): ").lower()
            if choice == "yes" or choice == "no":
                break
            else:
                print("Please enter only 'yes' or 'no'.")

        if choice != "yes":
            break  # Exit the loop if the user doesn't want to continue


if __name__ == "__main__":
    main()
