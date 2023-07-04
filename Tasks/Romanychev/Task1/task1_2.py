# Circle Area Calculator
# This program calculates the area of a circle based on the user-provided
# radius. The radius can be entered as an integer, fraction, decimal number,
# or scientific notation. If the area is very small (less than 0.01), a more
# precise value will be displayed. The program allows multiple circle area
# calculations until the user chooses to exit.


import math
import locale
from fractions import Fraction


def get_radius_from_user():
    while True:
        radius = input(
            "Enter the radius of the circle (as an integer, fraction, "
            "decimal number, or scientific notation): ")
        try:
            radius = float(radius)
            if radius <= 0:
                print("Please enter a positive number for the radius.")
            else:
                return radius
        except ValueError:
            try:
                radius = Fraction(radius)
                if radius <= 0:
                    print("Please enter a positive number for the radius.")
                else:
                    return radius
            except ValueError:
                try:
                    # Try to evaluate the input as scientific notation
                    radius = eval(radius)
                    if isinstance(radius, float) and radius <= 0:
                        print("Please enter a positive number for the radius.")
                    else:
                        return radius
                except:
                    print(
                        "Invalid input. Please enter a valid number, fraction,"
                        " or scientific notation.")


def calculate_circle_area(radius):
    return math.pi * radius**2


def format_area(area):
    if area == float('inf') or area == float('-inf'):
        return 'Infinity'
    elif area == 0:
        return '0'
    elif abs(area) < 0.01:
        return f"{area:.15f}"
    else:
        return locale.format_string("%.2f", area, grouping=True)


def main():
    # Set the default locale for formatting
    locale.setlocale(locale.LC_ALL, '')
    print("----------------------")
    print("Circle Area Calculator")
    print("----------------------")
    print("Instructions:")
    print("1. Enter the radius of the circle when prompted.")
    print("2. You can enter the radius as an integer, fraction, decimal "
          "number, or scientific notation.")
    print("3. For scientific notation, you can use either the 'e' or '*' "
          "notation.")
    print("4. Examples of valid inputs:")
    print("   - Integer: 5")
    print("   - Fraction: 3/4")
    print("   - Decimal number: 2.5")
    print("   - Scientific notation (using 'e'): 1.99e-26")
    print("   - Scientific notation (using '*'): 1.99 * 10**-26")
    print("   - Scientific notation (using 'e'): 2.5e30")
    print("   - Scientific notation (using '*'): 2.5 * 10**30")
    print("5. The program will calculate and display the area of the circle.")
    print("6. If the calculated area is very small (less than 0.01),"
          " it will be displayed in scientific notation.")
    print("7. After displaying the result, you will be asked if you want "
          "to calculate the area of another circle.")
    print("8. Enter 'Yes' to calculate the area of another circle, "
          "or 'No' to exit the program.")

    while True:
        radius = get_radius_from_user()
        area = calculate_circle_area(radius)

        formatted_area = format_area(area)
        if formatted_area == '0':
            print("A circle with a radius of zero (degenerate circle) is a "
                  "point - it is more of an exception than a rule.")
        else:
            print(f"The area of the circle is: {formatted_area}")

        choice = input(
            "Do you want to calculate the area of another circle? "
            "(Yes/No): ").lower()

        while choice not in ["yes", "no"]:
            choice = input("Invalid choice. Please enter Yes or No: ").lower()

        if choice == "no":
            print("Thank you for using the Circle Area Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
