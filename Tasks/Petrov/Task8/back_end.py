import json
import time


with open("anime_series.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

fields = ["title", "studios", "year", "genres"]

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


def filling_new_series(new_title):
    while True:
        new_series = [new_title]
        print("Fill the next parameters of this series:")
        try:
            for field in fields[1:]:
                value = input(f"{field} - ")
                if field == "year":
                    new_series.append(int(value))
                elif field == "genres":
                    new_series.append(value.split(", "))
                else:
                    new_series.append(value)
            return {field: value for field, value in zip(fields, new_series)}
        except ValueError:
            print("Wrong info for this field, error happened, try again")


def add_new_anime_series():
    new_title = input("Which anime series do you want to add? ")

    # to do - search_by_title(new_title)
    current_titles = [series["title"] for series in data.values()]
    if new_title in current_titles:
        print("This series is already in our storage")
    else:
        print("Okay")

        new_series = filling_new_series(new_title)
        new_pos = int(list(data.keys())[-1])+1
        data[str(new_pos)] = new_series
        with open("anime_series.json", "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=4)
        print("New anime series was added to storage")


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
