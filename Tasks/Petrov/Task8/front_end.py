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
        back_end.add_new_anime_series(new_title)  # to do false adding (cancel)
        print("New anime series was added to storage")


def search_anime_series():
    back_end.search_anime_series()
