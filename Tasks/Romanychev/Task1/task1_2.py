import math
from fractions import Fraction


def get_radius_from_user():
    while True:
        radius = input(
            "Enter the radius of the circle (as an integer, fraction, "
            "or decimal number): ")
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
                print("Invalid input. Please enter a valid number or "
                      "fraction.")


def calculate_circle_area(radius):
    return math.pi * radius**2


def main():
    print("----------------------")
    print("Circle Area Calculator")
    print("----------------------")

    while True:
        radius = get_radius_from_user()
        area = calculate_circle_area(radius)

        if abs(area) < 0.01:
            print(f"The value is very small - {area:.15f}")
        else:
            rounded_area = round(area, 2)
            print(f"The area of the circle is: {rounded_area}")

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
