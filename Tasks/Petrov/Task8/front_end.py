import time
import back_end


def separation():
    print("-"*30)
    time.sleep(1.5)


def welcome():
    print(back_end.greeting_message())
    separation()


def ending():
    separation()
    print(back_end.goodbye_message())


def process():
    while True:
        print("""What would you like to do?

        1. List all current anime series
        2. Add a new anime series to storage
        3. Search an anime series

        If you want to quit the program, just press Enter""", end="\n\n")
        action = back_end.action()
        print()
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
    print("Currently we have anime series such as:", end="\n\n")
    print('\n\n'.join(series for series in back_end.all_anime_series()))


def add_new_anime_series():
    new_title = input("Which anime series do you want to add? ")
    try:
        next(back_end.search_by_title(new_title))
        print("This series is already in our storage")
    except StopIteration:
        print("Okay")
        try:
            while True:
                print("Fill the next parameters of this series:")
                new_series = back_end.filling_new_series(new_title)
                back_end.add_new_anime_series(new_series)
                print("New anime series was added to storage")
                break
        except ValueError:
            print("Wrong info for this field, error happened, try again")


def search_anime_series():
    while True:
        try:
            print("""Choose field to search anime series from:

                1. Title
                2. Studios
                3. Year
                4. Genres

                5. Cancel the search""", end="\n\n")
            search_field = int(back_end.action())
            obj = back_end.fields[search_field-1]
            print(f"\n{obj} you're searching for:", end=" ")
            if search_field == 1:
                res = back_end.search_by_title(input())
            elif search_field == 2:
                res = back_end.search_by_studios(input())
            elif search_field == 3:
                res = back_end.search_by_year(int(input()))
            elif search_field == 4:
                res = back_end.search_by_genres(input().split(", "))
            elif search_field == 5:
                break
            else:
                raise ValueError
            print("\nThe following anime series were found: ")
            order = 1
            for item in res:
                print(f"\n{order}.", end=" ")
                anime = back_end.format_anime_series(item)
                print('\n'.join(line for line in anime))
                order += 1
            if order == 1:
                print("No search results")
            break
        except ValueError:
            print("Wrong input")
