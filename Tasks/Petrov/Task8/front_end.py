"""Module implements console UI for digital anime series storage"""

import time
import back_end


def separation():
    """Printing the line and waiting for visual part"""

    print("-"*30)
    time.sleep(1.5)


def welcome():
    """Printing the welcome message"""

    print(back_end.greeting_message())
    separation()


def ending():
    """Printing the goodbye message"""

    separation()
    print(back_end.goodbye_message())


def process():
    """Main UI function to manage the usage proccess"""

    while True:

        print("""What would you like to do?

        1. List all current anime series
        2. Add a new anime series to storage
        3. Search an anime series

        If you want to quit the program, just press Enter""", end="\n\n")

        action = back_end.action()
        print()

        # Processing the function based on selected option
        if action == "":
            break
        elif action == "1":
            list_all_anime_series()
        elif action == "2":
            add_new_anime_series()
        elif action == "3":
            search_anime_series()
        else:
            print("Uknown operation")

        separation()


def list_all_anime_series():
    """Printing all anime series in the storage"""

    print("Currently we have anime series such as:", end="\n\n")
    print('\n\n'.join(series for series in back_end.all_anime_series()))


def add_new_anime_series():
    """Describing the process of adding new anime series to the storage"""

    new_title = input("Which anime series do you want to add? ")
    try:

        # If anime series with such title was found, nothing will be added
        next(back_end.search_by_title(new_title))
        print("This series is already in our storage")
    except StopIteration:
        print("Okay")
        try:
            while True:

                # Filling other fields of the object
                print("Fill the next parameters of this series:")
                new_series = back_end.filling_new_series(new_title)

                # Adding new object to storage
                back_end.add_new_anime_series(new_series)
                print("New anime series was added to storage")
                break
        except ValueError:

            # Error for putting not an int for year
            print("Wrong info for this field, error happened, try again")


def search_anime_series():
    """Describing the process of searching an anime series from storage"""

    while True:
        try:
            print("""Choose field to search anime series from:

                1. Title
                2. Studios
                3. Year
                4. Genres

                5. Cancel the search""", end="\n\n")
            search_field = int(back_end.action())
            if search_field == 5:
                break
            field = back_end.fields[search_field-1]

            # Processing the search function based on selected search field
            print(f"\n{field} you're searching for:", end=" ")
            res = back_end.search_anime_series_by_field(field, input())

            print("\nThe following anime series were found: ")

            # Showing the search results to user
            order = 1
            for item in res:
                print(f"\n{order}.", end=" ")
                anime = back_end.format_anime_series(item)
                print('\n'.join(line for line in anime))
                order += 1

            # Printing the result if nothing was found (kinda)
            if order == 1:
                print("No search results")
            break
        except (ValueError, IndexError):

            # If something wrong was inputted
            # as option choice, ValueError raises
            # It also raises if the year was input incorrectly
            # If non-existing option was picked, IndexError raises
            print("Wrong input")
