import json
import time


with open("anime_series.json", "r", encoding="UTF-8") as file:
    data = json.load(file)


def separation():
    print("-"*30)
    time.sleep(1.5)


def greeting_message():
    print("Welcome to digital anime series storage!")


def goodbye_message():
    print("Thank you for using our storage, have a great day!")


def action():  # todo
    print("""What would you like to do?

          1. List all current anime series
          2. Add a new anime series to storage
          3. Search an anime series

          If you want to quit the program, just press Enter""", end="\n\n")
    return input("Your choice: ")


def list_all_anime_series():
    print("Currently we have anime series such as:", end="\n\n")
    for pos, series in data.items():
        print(f"{pos}.", end=" ")
        format_anime_series(series)
        print()


def format_anime_series(anime_series):
    for key, value in anime_series.items():
        if key == "title":
            print(value)
        elif key == "genres":
            print(f"{key}: {', '.join(genre for genre in value)}")
        else:
            print(f"{key}: {value}")


def add_new_anime_series():
    pass


def search_anime_series():
    pass


def search_by_title(title_seek):
    pass


def search_by_studios(studios_seek):
    pass


def search_by_year(year_seek):
    pass


def search_by_genre(genre_seek):
    pass
